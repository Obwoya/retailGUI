#!usr/bin/perl

$input = $ARGV[0];
$products = "products_local.sql";
$batchs = "batch_local.sql";
$promotion = "promotions.sql";
$prods_reg = "Reg_products.sql";
$warehouse_reg = "Reg_warehouse.sql";

open(input, $input) || die "Can't read from data file $!\n";
open(product, ">$products") || die "Can't create sql file $!\n";
open(promo, ">$promotion") || die "Can't create sql file $!\n";
open(batch, ">$batchs") || die "Can't create sql file $!\n";
# open(prod_reg, ">$prods_reg") || die "Can't create sql file $!\n";
# open(warehouse_reg, ">$warehouse_reg") || die "Can't create sql file $!\n";

$i = 000001;
$type = 0; #stands for bundle promotion
while($line = <input>) {
	chomp($line);

	#Each line is like Splash Pen:Incontinence Supplies:Jalna:89265520:66.60:3730:3430:0
	#Name:Category:Manufacturer:Barcode:CostPrice:CurrentStock:MinimumStock:BundleUnit
	#In database as barcode:name:category:maufacturer:cost
	@temp = split(/:/, $line);
	$stock = int $temp[6]/10;
	$cost = $temp[4]*1.25;
	$printline = "INSERT INTO product VALUES($temp[3],\"$temp[0]\",\"$temp[1]\",\"$temp[2]\",$cost,$stock,1);\n";
	print product $printline;
	#$printline = "INSERT INTO product VALUES($temp[3],\"$temp[0]\",\"$temp[1]\",\"$temp[2]\",$cost,$temp[6],0);\n";
	#print prod_reg $printline;
	#$printline = "INSERT INTO warehouse(barcode, stock) VALUES($temp[3],$temp[5]);\n";
	#print warehouse_reg $printline;
	$stock1 = int $stock/4;
	$stock2 = int $stock-$stock1;
	$printline = "INSERT INTO batch VALUES($temp[3],'2013-09-01',$stock1,NULL);\n";
	print batch $printline;
	$printline = "INSERT INTO batch VALUES($temp[3],'2013-09-15',$stock2,NULL);\n";
	print batch $printline;
	if($temp[7] != 0){
		$printline = "INSERT INTO promotion VALUES($temp[3],$i,$type,$temp[7],NULL,1);\n";
		$i++;
		print promo $printline;
	}

}
close(input);
close(product);
close(promo);
# close(prod_reg);
# close(warehouse_reg);