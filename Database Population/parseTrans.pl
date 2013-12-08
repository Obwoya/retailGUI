#!usr/bin/perl

$input = $ARGV[0];
$output1 = "transactionDetails.sql";
$output2 = "transaction.sql";
$output3 = "cashier.sql";

open(input, $input) || die "Can't read from data file $!\n";
open(transactionDetails, ">$output1") || die "Can't create sql file $!\n";
open(transaction, ">$output2") || die "Can't create sql file $!\n";
open(cashier, ">$output3") || die "Can't create sql file $!\n";

$trans = 0;
@cashiers = (0);
$numOfCashier = 0;
while($line = <input>) {
	chomp($line);

	#Each line is like 847214:8812:Mens Matrix Jacket:33995417:2:1/9/2013
	#TransactionId:CashierId:Name:Barcode:Units:Date
	#In database as id:barcode:date:promoid:quantity:price
	@temp = split(/:/, $line);
	@dates = split('/', $temp[5]);
	$date = $dates[2]."-".$dates[1]."-".$dates[0];
	$printline = "INSERT INTO transactiondetails VALUES($temp[0],$temp[3],NULL,$temp[4],\'sale\');\n";
	print transactionDetails $printline;

	if($trans != $temp[0]) {
		$trans = $temp[0];
		$cashier = $temp[1];
		$printline = "INSERT INTO transaction VALUES($trans, $cashier, \'$date\',0.00);\n";
		print transaction $printline;
	}

	$flag = 0;
	for($i=0; $i<$numOfCashier; $i++){
		if($cashiers[$i] == $temp[1]){
			$flag = 1;
			last;
		} 
	}
	if($flag == 0) {
		$cashiers[$numOfCashier] = $temp[1];
		$numOfCashier++;
		$printline = "INSERT INTO cashier VALUES($cashier,$numOfCashier, 1);\n";
		print cashier $printline;
	}
	
}

print $numOfCashier;
close(input);
close(transaction);
close(cashier);
close(transactor);