package main

import "fmt"

func main() {
	fmt.Println("Load Balancer")

	machinex := 1
	machiney := 0

	for {
		if machinex > machiney {
			if machinex >= 11 {
				machinex = 1
				calculox := ((machinex * 100) / 10)
				fmt.Println("Máquina X sobrecarregada - Porcentagem: ", calculox, "%")
				machiney = machiney + 1
			} else {
				calculox := ((machinex * 100) / 10)
				fmt.Println("Máquina X Sobrecarregada - Porcentagem: ", calculox, "%")
				machiney = machiney + 1
			}
		} else {
			if machiney >= 11 {
				machiney = 1
				calculoy := ((machiney * 100) / 10)
				fmt.Println("Máquina Y Sobrecarregada - Porcentagem: ", calculoy, "%")
				machinex = machinex + 1
			} else {
				calculoy := ((machiney * 100) / 10)
				fmt.Println("Máquina Y Sobrecarregada - Porcentagem: ", calculoy, "%")
				machinex = machinex + 1
			}
		}
	}
}
