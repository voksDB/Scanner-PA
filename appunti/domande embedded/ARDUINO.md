#### origine di Arduino

2003 all’Interaction Design Institute di Ivrea quando lo studente Hernando Barragán inizia a lavorare ad una tesi sotto la supervisione di Massimo Banzi e di Casey Reas

_Lo scopo del lavoro era la realizzazione di un ambiente di sviluppo software e hardware economico, semplice e completo,_ Le piattaforme embedded dei primi anni 2000 costavano alcune centinaia di dollari, i linguaggi usati erano “complessi” (C, C++, assembler!)

E’ riduttivo definire Arduino una semplice “board”, oggi infatti al nome Arduino si associa:
- una famiglia di board 
- alcuni ambienti di sviluppo 
- vari linguaggi di programmazione

La maggior parte del software e dell’hardware che gravita nell'ecosistema Arduino è “open”



#### pro e contro della piattaforma

___PRO___

- Le già citate _licenze_, che lo rendono un ambiente a bassissimo gap economico di ingresso
- altissimo livello di _community_, moltissime e utilissime _librerie_
- Una “_architettura_” sia dal punto di vista hardware e software, molto semplice. 
- Il linguaggio di programmazione ha una sintassi molto simile a C e Java, cioè i costrutti di base sono pressoché identici. 
- Fin dall'inizio, dato che l’oggetto doveva interfacciarsi col mondo fisico, la board originale offriva una _configurazione di “pin”_ di I/O (Input/Output), sia digitali (anche in PWM) che analogici, disposti secondo una collocazione che col tempo è diventata uno _standard_ de facto

___CONTRO___




#### spiegare meccanismo di boot di un Arduino (classico: UNO)

 
#### spiegare il funzionamento di setup() e loop()

#### panoramica tipi di dato

sai no tipo, int, string etc... ==cercare dati particolari==

#### panoramica operatori

#### cos'è un array?

#### spiegare direttive compilatore

panoramica costrutti di controllo di flusso

cos'è una funzione?
- descrivere il meccanismo di gestione degli interrupt facendo esempi di codice
- descrivere funzionalità del piedino AREF/VIN/D0-1-2-...-N/GND/A0-1-2-...-N/RX/TX/SDA/SCL/... di Arduino/Wemos/...
- spiegare differenza fra GPIO digitale e analogico