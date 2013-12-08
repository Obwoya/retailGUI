<?php

function dbconnect()
{
	$con = mysql_connect("localhost", "yatish", "null");
	mysql_select_db("3002local", $con);
	if(!$con)
	{
		die("Connection Failed!");
	}
	else{
		return $con;
	}
}

function dbclose($con)
{
	mysql_close($con);
}

//call to encrpt
function encrypt($sData, $sKey='54h6vhcg4c4gl'){ 
    $sResult = ''; 
    for($i=0;$i<strlen($sData);$i++){ 
        $sChar    = substr($sData, $i, 1); 
        $sKeyChar = substr($sKey, ($i % strlen($sKey)) - 1, 1); 
        $sChar    = chr(ord($sChar) + ord($sKeyChar)); 
        $sResult .= $sChar; 
    } 
    return encode_base64($sResult); 
} 

//call to decrypt. Use same sKey for encrypt and decrypt
function decrypt($sData, $sKey='54h6vhcg4c4gl'){ 
    $sResult = ''; 
    $sData   = decode_base64($sData); 
    for($i=0;$i<strlen($sData);$i++){ 
        $sChar    = substr($sData, $i, 1); 
        $sKeyChar = substr($sKey, ($i % strlen($sKey)) - 1, 1); 
        $sChar    = chr(ord($sChar) - ord($sKeyChar)); 
        $sResult .= $sChar; 
    } 
    return $sResult; 
} 


function encode_base64($sData){ 
    $sBase64 = base64_encode($sData); 
    return strtr($sBase64, '+/', '-_'); 
} 

function decode_base64($sData){ 
    $sBase64 = strtr($sData, '-_', '+/'); 
    return base64_decode($sBase64); 
} 


function createJson()
{
        $con = dbconnect();
        $posts = array();
        $response = array();
        $query = mysql_query("SELECT barcode FROM product");
        while($row = mysql_fetch_array($query))
        {
            $barcode = $row['barcode'];
            $qtyquery = mysql_query("SELECT SUM( unitsold ) FROM transactiondetails td, transaction t 
                    WHERE t.transactionid = td.transactionid 
                    AND DATE >= DATE_ADD( CURDATE( ) , INTERVAL -7 DAY ) 
                    AND DATE <= CURDATE( )  
                    AND type = 'sale' 
                    AND barcode =$barcode;");
            $qtyreq = mysql_fetch_array($qtyquery);
            $qtyreq = intval($qtyreq[0]);
            $qtyreq = intval($qtyreq/7);

            $holdingquery = mysql_query("SELECT stocklevel, active FROM product WHERE barcode = $barcode");
            $holdreq = mysql_fetch_array($holdingquery);
            $holdingreq = intval($holdreq[0]);
            $status = intval($holdreq[1]);
            $qtyreq = $qtyreq - $holdingreq;

            $salesquery = mysql_query("SELECT SUM( unitsold ) FROM transactiondetails td, transaction t 
                    WHERE t.transactionid = td.transactionid 
                    AND DATE = CURDATE( )  
                    AND type = 'sale' 
                    AND barcode =$barcode;");
            $salesreq = mysql_fetch_array($salesquery);
            $salesreq = intval($salesreq[0]);

            $writeoffquery = mysql_query("SELECT SUM( unitsold ) FROM transactiondetails td, transaction t 
                    WHERE t.transactionid = td.transactionid 
                    AND DATE = CURDATE( )  
                    AND type = 'write off' 
                    AND barcode =$barcode;");
            $writeoffreq = mysql_fetch_array($writeoffquery);
            $writeoffreq = intval($writeoffreq[0]);
            
            if($qtyreq <= 0) {
                    $qtyreq = 0;
            }
            if($status == 1) {
                    $enc_key = "AXCDSCFDSSXCVSS";
                    $posts[] = array('barcode'=>$barcode, 'quantity'=>encrypt($qtyreq), 'sales'=>encrypt($salesreq), 'write-off'=>encrypt($writeoffreq));
            }
        }

		$revenueQuery = mysql_query("SELECT SUM(t.price) FROM transaction t
        	WHERE t.date = CURDATE()");
        $totalrevenue = mysql_fetch_array($revenueQuery);
        $totalrevenue = $totalrevenue[0];
        
        $response['products'] = $posts;
        $response['total'] = encrypt($totalrevenue);
        
        //name file by shop id from settings file
        $filename = '1.json';
        
        $fp = fopen($filename, 'w');
        fwrite($fp, json_encode($response));
        fclose($fp);
        dbclose($con);

        return $filename;
}

function postFileToUrl($filename)
{
	$target_url = 'http://cg3002-20-z.comp.nus.edu.sg/api/upload.php';
        //This needs to be the full path to the file you want to send.
	//$file_name_with_full_path = 'C/shop/'.$filename;

	// password should match the one on regional
    $password =  "helloworld";
    //md5 hash it     
    $key  = md5($password);     
      
	$post = array('id' => '1', 'key' => $key, 'file_contents'=>'@C:\Users\yatishby\Desktop\Semester 5\CG3002\Project\retailGUI\1.json');
 
    $ch = curl_init();
	curl_setopt($ch, CURLOPT_URL,$target_url);
	curl_setopt($ch, CURLOPT_POST,1);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
	$result=curl_exec ($ch);
	$err = curl_errno($ch);
	curl_close ($ch);
	echo "Sent!!";
	//echo $result;
	echo $err;
}

function sendData()
{
	postFileToUrl(createJson());
}

?>