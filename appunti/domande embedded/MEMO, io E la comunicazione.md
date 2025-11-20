
#### differenze fra i vari tipi di memoria (RAM/ROM/flash/EPROM/sequenziale/casuale/SDRAM/DRAM/DDR/etc.)

- _Memoria ad accesso casuale (RAM)_: __volatile__ (ma non sempre) e generalmente “veloce”, di costo “elevato”, in grado di garantire il medesimo tempo di accesso per qualsiasi porzione di essa, associata alla memoria di sistema

- _Memoria ad accesso diretto_: __persistente__ e generalmente “lenta”, ma con un costo relativo più basso delle RAM,offre tempi variabili di accesso in base all'indirizzo di memoria a cui si vuole accedere. Di solito utilizzata per memorie di massa

- _Memoria ad accesso sequenziale_: Molto lenta, persistente, non particolarmente costosa, tempo di accesso molto variabile in base alla posizione attuale di lettura/scrittura. Utilizzata nei sistemi di backup a nastro

in un sistema embedded si identificano la memoria di sistema, o primaria e la memoria di massa: 


la __memoria di sistema__, RAM, si può distinguere in 3 tipologie principali: 

- _SRAM_: Definite anche come Static RAM, si tratta di una memoria statica, (non necessita di refresh), molto veloce, è utilizzata generalmente per delle memorie “cache”
- _DRAM_: Acronimo di Dynamic RAM, a tecnologia per memorie volatili assai più economica e semplice delle SRAM, ma che _richiede il refresh_, è asincrona( vedi sotto)
- _SDRAM_: E la variante sincrona delle DRAM (sta per Synchronous Dynamic RAM), la cui velocità è quindi collegata al clock del elaboratore, ampiamente _utilizzata nei sistemi desktop_/workstation (ad esempio la famiglia delle DDR ), da tempo viene utilizzata in misure e velocità diverse anche nei sistemi embedded di vario genere

Le __memorie di massa__ di dati persistenti, possono essere suddivise in base al tipo di supporto fisico utilizzato: 
- _ROM_: memorie in sola lettura, info contenuta nei transistor 
- _Flash Memory_: memorie NAND/NOR, chiavette USB... dischi a stato solido
- _Supporto Magnetico_: floppy e hard disk magnetici 
- _supporto ottico_: cd, dvd

___MEMORIE ROM___: 

Fin dai primordi delle tecnologie embedded, si è sempre fatto un utilizzo massivo delle cosiddette memorie ROM (Read Only Memory o memoria in sola lettura), le informazioni erano hard-wired ovvero codificate direttamente sul silicio, e _non riscrivibili successivamente_. 

ROM si sono evolute in diverse forme, aggirando, almeno in parte, il limite della impossibilità di riscrittura.

- _PROM_ (_Programmable_ read-only memory): PROM (Programmable read-only memory): Presenti sin dal 1956, le PROM sono memorie programmabili solo una volta tramite _l’uso di corrente elettrica ad alto potenziale_
- _EPROM_ (_Erasable_ Programmable read-only memory): A differenza delle PROM, le EPROM sono riscrivibili, ma solo un numero limitato di volte, “azzeramento” tramite luce ultravioletta. 
- _EEPROM_ (_Electrically_ Erasable Programmable read-only memory): 

le rom sono veloci in lettura (nel caso delle EEPROM molto lente in scrittura)


__FLASH MEMORY__: 

Le Flash Memory, di diretta derivazione delle EEPROM, si distinguono da queste ultime per la loro capacità di essere cancellate e riscritte a blocchi o unità più piccole e non interamente, 

progettate per prendere il posto delle EEPROM, quindi per contenuti che dovevano essere _letti di frequente, ma scritti di rado_ , , è stato preferito ottimizzarle per le lettura. 

- _NAND Memory_: I transistor sono collegati in un modo da creare un collegamento _in serie_ tra le celle, riduce lo spazio utilizzato sul supporto fisico, Sono memorie di gran lunga più economiche di quelle NOR. 

- _NOR Memory:_ Tutte le celle sono collegate a massa ed in parallelo alla bit line, ogni cella è _leggibile e scrivibile singolarmente_, ma occupa più spazio rispetto ad una cella di una memoria, una caratteristica delle NOR è che, nei processori che lo supportano, eventuale codice oggetto contenuto su di esse può essere eseguito sul posto (_Execution in Place_, __XIP__), ovvero senza il bisogno di essere caricato su una memoria esterna, Ciò la rende _ideale nelle fasi di boot_, dove la memoria di sistema potrebbe non essere ancora accessibile). Le NOR possono anche essere programmate per fornire un “random-access”, come le RAM.


nei sistemi embedded una memoria di tipo _NAND viene usata come storage principale_, ed una memoria _NOR_ utilizzata per funzioni a basso livello e di _boot_

==cercare differenza tra la porta nand e la porta nor==


#### cos'è e cosa fa una MMU?

_L’unità di gestione della memoria_ (Memory Management Unit, o MMU) è una particolare unità che si occupa prevalentemente di tre compiti:
- _TRADUZIONE INDIRIZZI VIRTUALI_: alcuni sistemi operativi non concedono l’utilizzo degli indirizzi fisici della RAM da parte delle applicazioni, gli indirizzi utilizzati sono insiemi separati di indirizzi virtuali (o logici), MMU fornisce un servizio di traduzione tra indirizzi logici e fisici
- _PROTEZIONE DELLA MEMORIA_: : il meccanismo di traduzione della memoria fa in modo che processi diversi non possano accedere alle medesime aree di memoria
- _GESTIONE DELLA CACHE_: in alcuni casi la MMU si occupa anche di gestire la memoria cache.


#### panoramica supporti memoria di massa nell'embedded, pregi e difetti

nei sistemi embedded una memoria di tipo _NAND viene usata come storage principale_, ed una memoria _NOR_ utilizzata per funzioni a basso livello e di _boot_

==come formulare questa domanda però??==

#### cosa si intende con XIP? pregi e difetti?

(execution in place) esecuzione in loco del codice, senza bisogno di caricarlo su di una memoria ram. 

==pregi e difetti?==

#### quali tipi di filesystem vengono usati nell'embedded? pregi e difetti

se la memoria ha controller, permettono l’utilizzo di filesystem ideati per dispositivi a blocchi quali gli hard-disk (FAT, NTFS, ext2/3/4).

Può succedere però che in alcune board, per motivi pratici o economici, tali controller vengano rimossi; in tal caso è necessario utilizzare dei tipi speciali di filesystem, ideati per gestire strutture basate sui cosiddetti “EraseBlock”, come ad esempio:

- _jffs1/2_: un “Log Structured Filesystem” disegnato per lavorare su NAND, ha alcuni limiti strutturali legati alla necessità di eseguire le fasi di clean ogni qual volta montato; 

- _yaffs1/2_: concettualmente simile ai filesystem JFFS, con il quale condivide alcuni limiti. Molto utilizzato dai produttori dei primi smartphone Android; 

- _ubifs_: di recente adozione, Ubifs introduce molte ottimizzazioni legate al “wear-leveling” e con minori tempi di accesso in fase di mount.

____


#### cos'è il "wear leveling"?

wear-leveling, Sistema per evitare che una memoria sia scritta sempre sullo stesso blocco. Senza questo sistema si potrebbe verificare la fine (per “consumo”) prematura del blocco stesso e di conseguenza la perdita di affidabilità della memoria, viene eseguita dal _controller_ della memoria un dispositivo

questo controller permettono l’utilizzo di filesystem ideati per dispositivi a blocchi quali gli hard-disk (FAT), Può succedere però che in alcune board, per motivi pratici o economici, tali controller vengano rimossi;

___

#### cos'è una RS232? che caratteristiche ha?

comunemente si riferisce alla RS232, come alla porta seriale, in realtà la sigla indica un preciso protocollo di comunicazione. 

Lo standard di riferimento per lungo tempo è stato il RS232-C, Ad oggi, l’ultima versione di questo standard è marchiata con il nome TIA-232-F, anche se i cambiamenti nei confronti della versione “C” sono limitati quasi solo ai segnali e al timing dei dispositivi. 

Le porte seriali, nel corso degli anni, sono state utilizzate come _interfacciamento_ per un grandissimo numero di dispositivi, quali _terminali, stampanti, mouse, tastiere, scanner, rete_, e fino a non molto tempo fa anche modem. 

Con l’avvento delle porte USB, le porte seriali sono progressivamente sparite dall'hardware desktop/workstation, ma sono rimaste sia in ambito embedded che in quello server, 

si può dire che su una linea seriale venga trasmesso _un solo bit alla volta_, e che il valore di questo singolo bit sia stabilito sulla base della _differenza di potenziale rispetto alla massa_ (GND). 

notare che l’intervallo che va da -3V a +3V è visto come segnale non valido (viene quindi ignorato), per eliminare il “rumore di fondo”, va da -15V(1) a +15V(0). 

al giorno d'oggi vengono usate seriali TTL (Transistor Transistor Logic), utilizzano bassa differenza di potenziale. 


#### descrivere NMEA0183

la _National Marine Electronic Association_, ente famoso nel mondo embedded per il noto standard NMEA0183: 

E’ uno standard sia _elettrico_ (cioè specifica i _livelli di tensione da utilizzare_ sui cavi usati per la comunicazione) sia “_protocollare_” (si potrebbe dire “applicativo”)

nato per inviare i dati degli strumenti di bordo quali GPS, bussole, profondimetri, etc. a bordo di un’imbarcazione. 

La specifica elettrica descrive un _bus seriale EIA-422, simile a RS-232_, ma con portata maggiore
RS-422 infatti usa un segnale elettrico “differenziale”, quindi con due cavi, per ogni via (TX e RX) mentre RS-232 usa un solo cavo per via, gli permette di essere più “robusto” (insensibile al rumore di fondo) e di poter raggiungere distanze maggiori senza perdere informazione.

La velocità ufficiale originale è _4800 baud(simboli al secondo) , oggi portata a 38400 baud)_ in cui un solo nodo (detto talker) può trasmettere e molti nodi (detti listener) possono ricevere.

I dati vengono trasmessi in ASCII (quindi human readable) e sono organizzati in stringhe (messaggi) ben formattate. Le stringhe hanno un formato vincolante definito sinteticamente come segue:

![[Pasted image 20251117171243.png]]



#### I2C vs. SPI

__I2C__

si legge $I^2C$, acronimo di inter-integrated-circuit è un _bus seriale_, ideato per la comunicazione a breve distanza all'interno dello stesso computer embedded. 

I2C utilizza _due linee bidirezionali_ (open-drain) note come SDA (Serial Data Line) e SCL (Serial Clock Line) per interconnettere tra di loro alcuni nodi. I nodi all'interno del bus possono avere due distinti ruoli: 
- _Master_: Genera il clock e fa partire la comunicazione con lo slave; 
- _Slave_: Riceve il clock e risponde quando indirizzato dal master.

I2C è un bus “_multi-master_”, ovvero dove è possibile la presenza di più nodi master. Inoltre il ruolo master/slave può essere variato tra un messaggio e l’altro.
![[Pasted image 20251117173615.png]]

esistono varie velocità possibili sul canale: 

standard mode 100 kbit/s 
Fast mode 400 kbit/s 
Fast mode plus (Fm+) 1 Mbit/s 
High Speed Mode 3.4 Mbit/s 
Le velocità più alte sono disponibili solo nelle ultime versioni del BUS, e sono tipiche dei sistemi embedded.

![[Pasted image 20251117173559.png]]
il segnale del clock (SCL) viene abilitato ogni volta che si intenda mandare un singolo bit,

- Sulla linea dati (SDA), dopo la condizione S di start (SCL attivo, SDA disattivato) viene specificato un indirizzo di destinazione da 7 bit più un ulteriore singolo bit atto ad indicare se si tratti di una operazione di read (lettura) o write (scrittura), 
- . A questo deve seguire un segnale di ACK da parte dello slave. `bok!`
- dopo avviene la trasmissione del dato vero e proprio, impacchettato in una o più trame da 8 bit l’una, seguite ogni volta da un altro segnale di ack dallo slave
- la fine della trasmissione è marcata dalla "stop condition" (la P)

__SPI__

Serial Peripheral Interface, è la specifica di un bus per comunicazione _asincrona_, per comunicazioni a breve distanza e velocità bassa. 
è di tipo master/slave, ma non multi-master come I SQUARE C.  

è basata su 4 segnali: 
![[Pasted image 20251117175312.png]]

- _SCLK, serial clock_: è un segnale inviato dal master e controlla lo spostamento di bit tra master e slave
- _IL MISO_, è collegato da in Master e out Slave
- _il MOSI_ è il contrario in Slave e Out Master
- _IL CS (chip select)_ è utilizzato per selezionare il chip slave che deve essere abilitato alla comunicazione dal master. (unico o multiplo

a meno che non venga specificato, non ci sono condizioni di inizio e fine trasmissione ne segnali di ack. 

#### a cosa serve una linea di CLOCK? se ne può fare a meno?

==a sincronizzare la comunicazione?== 

sicuramente se ne può fare a meno, ma è più facile connettere per bene mi sa. 

#### vantaggi e svantaggi del "chip select"

==non sono elencati sul libro, chiedere a chat gpt== 

___

#### tutto quello che sai sui GPIO

Un GPIO (_General Purpose Input/Output_) è la rappresentazione di un pin e del segnale digitale che passa transita su di esso.

è possibile definire i due stati di un GPIO, “alto” o “basso” in base alla presenza di una determinata tensione sul _pin_

e si immagini che sul pin associato al GPIO vi possa essere una tensione che varia da 0V a $V_{ref}$
Quando la tensione sul pin è prossima ad un intorno di V_ref , il GPIO è nello stato “alto”. 

Tale associazione tra valori logici e stati è vera qualora i GPIO siano configurati nella cosiddetta modalità “_attivo alto_” (o active-high) analogamente esiste anche la configurazione "attivo basso". 

Frequentemente, durante la progettazione di un SoC, i pin non utilizzati da altri device vengono allocati come GPIO. 

Le _modalità di utilizzo_ dei GPIO sono le seguenti:
- _Input_: Il GPIO è utilizzato per leggere valori binari dal pin
- _Output_: Il GPIO è utilizzato per scrivere sul pin valori binari
- _IRQ_: Si tratta di una particolare modalità di input in cui la variazione di valore sul pin viene utilizzata per scatenare _interrupt_ all'interno del sistema

i GPIO possono essere utilizzati per il monitoraggio di presenza per una scheda SD/MMC, il controllo di led e pulsanti, bit banging, ricezione e invio di segnali. 

#### cosa si intende con "sink" nel contesto dei GPIO?

==non sul libro==

#### cosa si intende con input "floating"

==non sul libro==

#### cos'è il "bouncing" e quali tecniche si usano per arginare il problema?

==non sul libro==
#### pullup e pulldown

==sono sicuro che ci sia sul libro,ma non spiegato bene==

#### cos'è il "bit banging"? vantaggi e svantaggi

Il “bit banging” è una tecnica per _implementare comunicazioni seriali generando treni di impulsi via software_, evitando qualunque tipo di hardware specifico, Si basa sul fatto che i processori odierni, anche per l’embedded, sono abbastanza veloci da poter “emulare” un circuito dedicato alla generazione di segnali non eccessivamente complessi.

per inviare su una linea seriale un treno di impulsi corrispondente ad un byte è sufficiente “ciclare” su tutti i bit del byte stesso alzando (HIGH) il piedino di output utilizzato ogniqualvolta si incontra un “1”. 

ha il vantaggio di essere molto semplice ed economico, non bisogna usare hardware dedicato 

il problema si ha nell'assicurare una comunicazione efficace, il "ciclo" dei bit deve essere eseguito con velocità regolare, o bisogna avere una linea separata per il clock per sincronizzare. 
l’implementazione software viene infatti influenzata da ciò che sta girando sul device, ad esempio la gestione degli interrupt potrebbe “distrarre” il processore abbastanza a lungo da far perdere dati.
#### cos'è il JTAG? (Joint Test Action Group)

JTAG è uno strumento fondamentale per lo sviluppo di dispositivi embedded, adattato per lo più universalmente in tantissime _development board e validation board per il testing e validazione_ sia hardware che software

Nel 1985 il consorzio di aziende nord americane ed europee chiamato Joint Test Action Group
propose la metodologia definita come Boundary Scan, è stata formalizzata nello standard IEEE nel 1990 intitolato Standard Test Access Port and Boundary-Scan Architecture 

si può pensare al JTAG come una linea di _celle interconnesse_ messa tutta intorno alla logica input/output del chip, Queste celle, _in condizioni normali rimangono non operative_, e lasciano transitare i segnali di input/output.
Quando, attraverso il cosiddetto _TAP(Test Access Port)_ Controller si abilita il bypass, le celle possono raccogliere le informazione sullo stato complessivo dei registri e della memoria

Tutto questo di solito è sfruttato attraverso specifici connettori JTAG e le cosiddette probe
di collegamento tra la board di sviluppo ed il computer utilizzato per effettuare il debug