# holdingssummary

This code converts the MFHD 863 tag to NISO standard. This can be batch-added to the MFHD in the 866 tag (summary of holdings). This is useful if your serials records are missing the summary of holdings.

The holdings must be single line for the programs to work.

I recommend using the MARCedit Export Tab Delimited tool to create a text file of MFHD data. The file should be comma delimited:
MFHDID, 852 tag, 863 tag.

1393, 23$81$av.$i(year), 40$81.5000$a36$i1983
1881, 23$81$av.$i(yr.), 40$81.5000$a12$i1983
2481, 23$81$av.$i(year), 40$81.5000$a2$i1979
4638, 23$81$ano.$i(year), 40$81.1$a48$i1983
4795, 23$81$av.$i(yr.), 40$81.1$a152-154$i1983
4796, 23$81$av.$i(yr.), 40$81.1$a155-157$i1983
5900, 23$81$a(year), 40$81.5000$a1983

