i0x03. Shell, init files, variables and expansions >> TASKS

Binary >> Decimal: echo $((2#BINARY_NUMBER))
Octa >> Decimal: echo $((8#OCTA_NUMBER))
Hexa >> Decimal: echo $((16#HEXA_NUMBER))

Decimal >> Binary: echo "obase=2;DECIMAL_NUMBER" | bc
Decimal >> Binary: echo "obase=8;DECIMAL_NUMBER" | bc
Decimal >> Binary: echo "obase=16;DECIMAL_NUMBER" | bc
