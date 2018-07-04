#! /usr/bin/env python

file = open("CHG029162.ready.snp.vcf","r")
result = open("chrYPASS100.vcf","w")
for eachline in file:
    line = eachline.split("\t")
    if line[0] == "chrY" and line[6] == "PASS":
        list = line[9].split(":")
        if int(list[2]) > 100:
            result.write("%s" % (eachline))
file.close()
result.close()