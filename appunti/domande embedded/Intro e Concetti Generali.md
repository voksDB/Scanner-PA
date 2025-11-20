
### Intro 

#### Definizione di sistema embedded 

> Con la terminologia Sistema Embedded (tradotto testualmente “sistema incorporato”) si tende ad indicare _l'insieme composto da hardware e software_ (occasionalmente deﬁnito ﬁrmware) dedicato a _speciﬁci scopi_ (“specific purpose”) i cui elementi siano tutti quanti integrati ed incorporati

è una definizione molto generica, un esempio di sistemi che rientrano: 

- stampanti 
- pos e bancomat 
- dispositivi IOT
- router, switch, dispositivi di rete 
- elettrodomestici e domotica 

#### panoramica generale sui sistemi embedded, classi di device, caratteristiche, ordini di grandezza (dimensioni, potenze, consumi, ecc.), ambiti di utilizzo

> È possibile infatti fornire una prima suddivisione sulla base del tipo di elaboratore utilizzato in _tre macro-gruppi_:
 - PLC (Programmable Logic Controller)
 - Microcontrollori
 - SoC (System-on-Chip)


I _PLC_ (o _Programmable Logic Controller_) sono dei dispositivi relativamente semplici, generalmente pensati per lavorare su sistemi di automazione e non destinati alla produzione su vasta scala; in molti casi vengono programmati individualmente per svolgere una sola funzione specifica.

Sono generalmente dotati di una buona connettività input/output per consentire la possibilità di interazione con sensori di vario genere

Per quanto i vari prodotti sul mercato condividano i concetti base di programmazione dei PLC, tali dispositivi non sono interscambiabili o compatibili tra di loro.

_Microcontrollori o MCU_, sono nati con l'idea di fornire un sistema hardware general purpose, 
fornendo un sistema hardware completo all'interno del singolo chip. 
Sin dai primi sviluppi, su alcuni modelli era possibile caricare del software adattato allo scopo designato su una apposita EPROM. 

basse prestazioni, ma altrettanto basso consumo energetico (100MHz - inferiori a 1W) e soprattutto basso prezzo. 

usati come sistemi di controllo, in generale possono svolgere le stesse funzioni dei PLC ma hanno più alta versatilità. 

_le info sulle soc sono nella domanda sottostante_

#### componenti interni di un MCU (MicroController Unit)

- Unità di elaborazione
- Memoria dati (RAM o EPROM) 
- Oscillatore (esterno o interno) 
- Memoria programma (ROM, EPROM, FLASH) 
- GPIO (General Purpose Input Output)
- Porte di comunicazione base (USART, I2S, SPI, I2C, USB)
- Porte analogiche (DAC, ADC, PWM)



#### definire SoC, cosa contiene, come si "combina" per la realizzazione dei vari prodotti reali

> i _SoC (system on chip)_, gamma di prodotti dalle maggiori potenze computazionali rispetto ai PLC e alle MCU e da dotazioni assai più ricche, singole unità che al loro interno contengono tutte o quasi le componenti del sistema, CPU, GPU, RAM, Memoria, Dispositivi per la connettività (BT/wifi/Ethernet) input/output Audio e Video.....  

in base al costo e allo scopo di elezione, è possibile trovare un sottoinsieme di questa componentistica.

I SoC sono utilizzati praticamente ovunque, sia in ambito automotive, militare, domotico , Set Top Box (lettori multimediali, televisori, sistemi di “infotainment” domestici e da viaggio)

ARM e MIPS, sono state le due grandi architetture di riferimento nel settore dei SoC. 

___

### Concetti Generali 

#### sistemi monoprogrammati e multiprogrammati, differenze, caratteristiche, cosa c'entra la MdT?

Una architettura semplice che si può immaginare per un computer è una più o meno elaborata _Macchina di Turing_(MDT). 
![[Pasted image 20251112145351.png]]

a MdT è composta da una “macchina a stati”4 dotata di una o più testine/cursori che leggono e scrivono simboli su uno o più nastri

esegue in continuazione il seguente loop: 

- legge il simbolo sotto al cursore 
- interpreta il simbolo secondo la macchina a stati interna 
- sposta il cursore
- (opzionalmente, prima o dopo lo spostamento) scrive un simbolo sul nastro 

e ad esempio volessimo tracciare un parallelo fra MdT e computer potremmo dire che la macchina a stati è la CPU, un nastro è memoria , l’alfabeto dei simboli sul nastro è rappresentato da numeri binari

questo è un sistema monoprogrammato, esegue solo quel programma, In una MdT, per _cambiare comportamento_ (programma), bisogna sospendere il loop, riscrivere la parte di nastro contenente il programma e riavviarla

> da chat 

Un **sistema monoprogrammato** è un sistema in cui **viene eseguito un solo programma alla volta**. Tutte le risorse del sistema — CPU, memoria, dispositivi di I/O — sono dedicate esclusivamente a quel programma fino al suo completamento.  
Esempi tipici sono i **sistemi embedded semplici**

Un **sistema multiprogrammato**, invece, consente **l’esecuzione concorrente di più programmi**, più processi vengono caricati in memoria e il processore **li alterna rapidamente**, grazie a un **meccanismo di scheduling** gestito dal sistema operativo.

Quando un processo è in attesa (ad esempio per un’operazione di I/O), un altro può utilizzare la CPU, migliorando l’**utilizzo delle risorse** e l’**efficienza globale** del sistema.


#### conversione AD e DA, caratteristiche, pregi e difetti, considerazioni sul flusso di dati campionati. 

 > processi di _trasformazione dei segnali_ che permettono il trattamento dei segnali _analogici_ (mondo reale, fisico) da parte di sistemi _digitali_ (computer).

> la conversione AD, il segnale analogico in ingresso viene “_campionato_”, cioè misurato a intervalli regolari, 

`good to know: `

La “_frequenza di campionamento_” è la velocità con cui si fanno le misure, ed indica il numero di letture nell'unità di tempo. 

Il suo inverso, il “_tempo di campionamento_” specifica l’intervallo fra una misura e l’altra.

più alta la frequenza, meglio si riesce a rendere la fedeltà del segnale

> La conversione DA è il processo inverso rispetto alla AD, si tratta in questo caso di _generare un segnale continuo a partire da una sequenza di valori_ (misure). 

per farlo si utilizzano dei generatori programmabili di tensione.

==ci starebbe dire qualcosa in più sulla DA== 


#### spiegare tecniche di multiplexing (divisione tempo, frequenza), shift register

> Il concetto di multiplexing comprende le metodologie per condividere un _canale fisico_ per trasportare più flussi informativi contemporaneamente (pagando in termini di complicazione tecnica, banda passante, rumore, ecc.)

si sviluppano dalla necessità di gestire informazioni provenienti da sensori (o inviate ad attuatori) in numero maggiore rispetto alla disponibilità di ingressi/uscite 

2 tecniche principali: 

_divisione di frequenza:_ i segnali da trasmettere contemporaneamente vengono inviati sul canale usando frequenze diverse, ognuno dei riceventi deve sintonizzarsi sulla frequenza che gli compete come nel caso delle trasmissioni radio. 

il ricevente, il de-multiplexer insomma, redistribuisce l'informazione smistando le comunicazioni. 

_divisione di tempo:_ i segnali da trasmettere “contemporaneamente” vengono inviati sul canale in alternanza veloce, Il canale è **suddiviso in intervalli di tempo**, È tipico delle **trasmissioni digitali** e dei **sistemi embedded** con bus condivisi, L’ordine e la sincronizzazione sono fondamentali: un clock o un protocollo temporale gestisce l’alternanza.

Lo **shift register (registro a scorrimento)** entra in gioco **nella realizzazione pratica del multiplexing**, è componente hardware che lo rende possibile: prende dati paralleli e li “spinge” fuori uno per volta, realizzando di fatto una trasmissione multiplexata nel tempo.

- In un sistema embedded con un microcontrollore che deve inviare 8 segnali digitali su **una sola linea**, si usa uno **shift register seriale** per “spostare” i bit in uscita in sequenza temporale.
    
- Allo stesso modo, in ricezione, un **shift register parallelo** ricompone i bit ricevuti in parallelo.

#### differenza fra controllo a loop chiuso e aperto, problemi del loop aperto
![[Pasted image 20251112160707.png]]
no feedback :(


![[Pasted image 20251112160720.png]]
si feedback :) 


La differenza tra i due modelli è che in quello senza retroazione il comportamento atteso del sistema è hardcoded, _non c’è nessuna “lettura” (feedback) dell’effettiva efficacia dell’azione_, mentre nel modello a retroazione è possibile codificare azioni correttive in funzione dell’output effettivamente ottenuto.

Infatti il modello open loop può essere utilizzato solo nei casi in cui è possibile scrivere una funzione corretta, come ad esempio nel caso di una lampadina o di un LED in cui la luminosità non è praticamente influenzata da fattori esterni e dipende solo dalla tensione di alimentazione

nell'open loop il costo di progettazione risiede nel perfezionamento della formula, nel modello closed loop si deve studiare al meglio il meccanismo di feedback

==saper un po' spiegare la tecnica della pwn utilizzata nella lezione== 
#### spiegare tecnica PID per controllo a loop chiuso

potendo far riferimento all'efficacia dell’azione, le variabili di uscita, può realizzare la c.d. “correzione del tiro”. 

`DTK:` una gestione troppo reattiva può causare oscillazioni, una troppo lenta non reagisce in tempo

_PID_ (Proporzionale-Integrativo-Derivativo)

Il “controllo PID” modella la funzione di trasferimento come una somma pesata di tre componenti dipendenti dalla “funzione di errore”
- _distanza assoluta_ dallo stato desiderato P 
- la _storia dell’evoluzione dello stato_ del sistema I
- _velocità_ di variazione dello stato D

![[Pasted image 20251112162652.png]]
a funzione della componente _integrativa_: serve a (tentare di) raggiungere più rapidamente l’obbiettivo se si è “partiti da lontano”, la componente integrativa calcola la media degli errori da quando il sistema è stato attivato

la componente _derivativa_ valuta la velocità di allontanamento/avvicinamento all'obbiettivo.

la componente _proporzionale_ utilizza l’errore “istantaneo”/attuale per valutare quanto il sistema sia lontano dall'obbiettivo

esempio del motore: 
e(t) = GiriMotore − RegimeDesiderato


#### considerazioni sull'uso della memoria in un Arduino (Harvard), rispetto ai tipi di dati disponibili

la memoria nel contesto “embedded” è di gran lunga inferiore a quella a cui si potrebbe essere abituati, pochi kilobyte di RAM, e  si dovrà ragionare molto bene e a priori sul numero e sul tipo delle variabili dichiarate nel corso del programma stesso. 

- utilizzare variabili semplici quando possible 
- considerare l'utilizzo delle librerie, dove a volte non è possible sapere a priori il costo
- occhio alle invocazioni delle funzioni 
- E non va dimenticata la “memoria di programma” cioè lo spazio impegnato dal codice compilato: il “codice binario” che viene caricato sulla board occupa spazio

molti sistemi embedded espongono architetture estremamente semplici, e nei sistemi più compatti _è raro avere a disposizione una MMU (Memory Management Unit)_
tutti gli accessi alla memoria non sono controllati se non dal programmatore stesso. 

- accesso ad un array: _sforare_ l’indice vuol dire andare a leggere/scrivere in zone di memoria non previste
- _sforamento stack/heap_: riempire lo stack oltre il suo limite (andando quindi a “coprire” parte dello heap) non scatena nessun “avviso”, anche in questo caso gli effetti sono potenzialmente catastrofici (idem).

#### architettura Von Neumann vs. Harvard

==da chiedere bene a chat gpt dai==

#### argomentare validità della ricorsione in ambito embedded, vantaggi e svantaggi

- vantaggi non ne vedo, svantaggio è quello che occupa un botto di memoria 

#### descrivere la gestione della memoria in un sistema embedded

- per ora come sopra, la gestione è affidata al programmatore 
#### spiegare meccanismo dell'interrupt (specie in ambito ESP8266/32)

 > È possibile semplicemente “_agganciare_” una funzione all'arrivo di un segnale su una determinata porta, tale funzione verrà eseguita, interrompendo temporaneamente l’esecuzione normale del programma, alla ricezione del segnale.
==cercare altro al capitolo 4==

in esp: 

- Si può associare una **ISR a un pin** specifico, in modo che venga eseguita quando il segnale cambia stato (ad esempio su fronte di salita o discesa).
- L’ISR deve essere **molto breve e non bloccante**, perché viene eseguita in un contesto di alta priorità. ( non si devono mettere delay)
- È possibile usare **attachInterrupt()** in Arduino framework,

si ricorre spesso al cosiddetto “multitasking cooperativo”. Il multitasking cooperativo
Ogni funzione-task deve essere breve (perché altrimenti mantiene il controllo per troppo tempo e fa sforare l’invocazione temporizzata delle altre) e deve, ove opportuno, saper gestire uno “stato” memorizzato in alcune variabili per poter lavorare “iterativamente" 
#### spiegare licenza proprietaria vs. libera

il software proprietario viene rilasciato comunemente con licenze restrittive chiamate genericamente _EULA(End User License Agreement)_


per quanto questo tipo di licenza sia molto comune, in realtà ogni software proprietario ha una sua propria variante, scritta dell’azienda che rilascia il software, generalmente hanno in comune: 

- _Divieto di far girare il programma su più dispositivi_, In altri casi le aziende optano per una sola licenza di sfruttamento con il pagamento di una royalty47 per ogni dispositivo utilizzato.
- _Divieto di fare reverse engineering_, 
- _Divieto di rivendere il programma_
- _Divieto di studiare le prestazioni_ del programma e di fare confronti con altri programmi e di pubblicare i risultati.
- _Divieto di modifica_

Software Libero e Open source

Le licenze libere per il software sono quelle che rispettano e proteggono le seguenti libertà fondamentali: 
- _Libertà di eseguire_ il programma come si desidera, per qualsiasi scopo. 
- _Libertà di studiare_ come funziona il programma e di modificarlo in modo da adattarlo alle proprie necessità. L’accesso al codice sorgente ne è un prerequisito.
- _Libertà di ridistribuire copie_ in modo da aiutare il prossimo.
- Libertà di _migliorare il programma e distribuirne pubblicamente i miglioramenti_ da voi apportati (e le vostre versioni modificate in genere), in modo tale che tutta la comunità ne tragga bene

la GNU GPL (GNU51 General Public License) nelle sue molteplici varianti rappresenta l’esempio più celebre di questa filosofia. 


il concetto di _Open Source_ differisce per definizione da quello di Software Libero, fornendo dei criteri simili ma non identici: 
- _Ridistribuzione libera_. La licenza non può impedire ad alcuna parte in causa la vendita o la cessione del software. Chiunque deve poter fare tutte le copie che vuole, venderle o cederle, e non deve pagare nessuno per poter fare ciò.
- il programma deve _includere il codice sorgente_
- la licenza deve permettere le modifiche e consentire la distribuzione di _opere derivate_
- _integrità del codice sorgente_, la licenza può proibire la distribuzione di opere derivate
- la licenza deve essere applicabile per tutti _senza discriminazione_  per persone o gruppi 
- _nessuna discriminazione di settori_. Analogamente alla condizione precedente, questa impedisce che si possa negare la licenza d’uso in determinati settori, per quanto questi possano essere deplorevoli. Non si può dunque impedire l’uso di tale software per produrre armi chimiche o altri strumenti di distruzione di massa.
- La licenza non dev'essere specifica a un prodotto.
- La licenza non deve contaminare altro software.
- La licenza deve essere tecnologicamente neutra


e il Software Libero si concentra su valori etici e filosofici, mentre l’Open Source è legato a criteri pratici di sviluppo e rilascio.


#### fare esempio di licenza software libera, descrivendone le caratteristiche salienti

come sopra la GNU. e aggiungendo: 
 la licenza GNU (come la GPL) impone che il software derivato debba mantenere la stessa licenza, garantendo che rimanga libero e open source. Questo concetto, chiamato [copyleft](https://www.google.com/search?q=copyleft&oq=la+licenza+gnu+ha+l%27obbligo+di+mantenere+la+stessa+licenza+nel+software+derivato%3F+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCjI5MjkwajBqMTWoAgiwAgHxBeCWV8oZYY0G8QXgllfKGWGNBg&sourceid=chrome&ie=UTF-8&mstk=AUtExfBsIeIGf6n81N14dZWrgcjFfusc1wNYrysSFS_YgEd5ypJJHAR7sDfAamXlg3x1cdYFvTDMOH3GWcUi98_MZJFw9gApZkfgkO82mfx4_a3HvyUj54TMPsMDNroc7ooSYR1zRq4_aj2m4OHKPiKBNMTc6AwW9nyjrO6_wDsthDCbg2M&csui=3&ved=2ahUKEwjFg7bOh-2QAxWV_7sIHSY1AHUQgK4QegQIARAC),assicura che le libertà di usare, studiare, modificare e distribuire il software siano preservate anche nelle versioni successive.


#### descrivere il concetto di watchdog

> da chat 

è un **meccanismo di sicurezza hardware o software** usato nei sistemi embedded per **rilevare e correggere blocchi o malfunzionamenti** del programma.

**timer autonomo** che il programma deve **periodicamente azzerare o “rinfrescare”** per dimostrare che sta funzionando correttamente,altrimenti il  microcontrollore esegue **un reset automatico del sistema**.

> dal libro

![[Pasted image 20251119163942.png]]

