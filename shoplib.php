<?php

function dbconnect()
{
	$con = mysql_connect("localhost", "yatish", "null");
	mysql_select_db("3002local", $con);
	ini_set('max_execution_time', 600);
	if(!$con)
	{
		die("Connection Failed!");
	}
	else{
		return $con;
	}
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
	$qtyreq = 5;
	$posts = array();
	$response = array();
	$query = mysql_query("SELECT barcode FROM product");
	while($row = mysql_fetch_array($query))
	{
	$barcode = $row['barcode'];

	$checkIfTrans = mysql_query("SELECT count(*) FROM TransactionDetails td, Transaction t 
			WHERE t.transactionID = td.transactionID 
			AND t.DATE = CURDATE()   
			AND barcode =$barcode;");
	$isThereAny = mysql_fetch_array($checkIfTrans);
	$isThereAny = $isThereAny[0];
	if ($isThereAny > 0) {
		$qtyquery = mysql_query("SELECT SUM( unitsold ) FROM TransactionDetails td, Transaction t 
				WHERE t.transactionID = td.transactionID 
				AND t.DATE = CURDATE( )   
				AND barcode =$barcode;");
		$qtySold = mysql_fetch_row($qtyquery);
		$qtySold = $qtySold[0];

		$qtyreq = $qtySold;
		
		$enc_key = "AXCDSCFDSSXCVSS";
		$posts[] = array('barcode'=>$barcode, 'quantity'=>encrypt($qtyreq));
		}
	}
	
	$response['products'] = $posts;
	
	//name file by shop id from settings file
	$filename = '0.json';
	
	$fp = fopen($filename, 'w');
	fwrite($fp, json_encode($response));
	fclose($fp);

	return $filename;
}

function postFileToUrl($filename)
{
	$target_url = 'http://172.28.180.133/api/upload.php';
        //This needs to be the full path to the file you want to send.
	$file_name_with_full_path = './'.$filename;

	// password should match the one on regional
    $password =  "helloworld";
    //md5 hash it     
    $key  = md5($password);     
      
	$post = array('id' => '0', 'key' => $key, 'file_contents'=>'@'.$file_name_with_full_path);
 
    $ch = curl_init();
	curl_setopt($ch, CURLOPT_URL,$target_url);
	curl_setopt($ch, CURLOPT_POST,1);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
	$result=curl_exec ($ch);
	curl_close ($ch);
	echo "Sent!!";
	echo $result;
}


function sendData()
{
	postFileToUrl(createJson());
}

function invert($num)
{
	if($num == 0){
		$num = 1;
	} else {
		$num = 0;
	}
	return $num;
}


function getData() {
	$url = 'http://cg3002-20-z.comp.nus.edu.sg/api/download/1-fc5e038d38a57032085441e7fe7010b0.json';
	$con = dbconnect();
	//$url = 'http://localhost/3002local/0-fc5e038d38a57032085441e7fe7010b0.json';
	$json = file_get_contents($url);
	$data = json_decode($json, true);
	
	foreach($data['product_list'] as $product) 
	{
		$barcode = ($product['barcode']);
		$name = decrypt($product['name']);
		$category = decrypt($product['category']);
		$manufacturer = decrypt($product['manufacturer']);
		$price = round(decrypt($product['costprice']), 2);
		$active = invert(decrypt($product['deleted']));
	
		$query = mysql_query("SELECT count(*) FROM Product WHERE barcode='$barcode'");
		$count = mysql_fetch_row($query);
		$count = $count[0];
		if($count > 0)
		{
			$query = mysql_query("SELECT count(*) FROM Product WHERE barcode=$barcode AND name='$name' AND category='$category' AND manufacturer='$manufacturer' AND cost=$price AND active=$active");
			$requireUpdation = mysql_fetch_row($query);
			$requireUpdation = $requireUpdation[0];
			if($requireUpdation == 0)
			{
				mysql_query("UPDATE Product SET name='$name', category='$category', manufacturer='$manufacturer', cost=$price, active=$active WHERE barcode=$barcode");
				//echo "UPDATE Product SET name='$name', category='$category', manufacturer='$manufacturer', cost=$price, active=$active WHERE barcode=$barcode"."<br>";
			}
			else
			{
				//echo "Not added"."<br>";
			}
		}
		else
		{
			mysql_query("INSERT INTO Product(barcode,name,category,manufacturer,cost,stocklevel,active) VALUES ($barcode,'$name','$category','$manufacturer',$price,0,$active)");
			//echo "INSERT INTO Product(barcode,name,category,manufacturer,cost,stocklevel,active) VALUES ($barcode,'$name','$category','$manufacturer',$price,0,$active)"."<br>";
		}			
	}
	echo "finished product list";
	
	foreach($data['shipment_list'] as $ship) 
	{
		$barcode = ($ship['barcode']);
		$quantity = decrypt($ship['quantity']);
	
		$query = mysql_query("SELECT * FROM Product WHERE barcode=$barcode");
		if(mysql_num_rows($query) > 0)
		{
			mysql_query("UPDATE Product SET quantity=$quantity WHERE barcode=$barcode");
		}			
	}
	echo "finished shipping list";
	mysql_query("UPDATE flag SET flag=1 WHERE 1");
}
?>