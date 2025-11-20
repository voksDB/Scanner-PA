## Intro: tutto, in dettaglio.

  

NOTABENE: NON SONO RISPOSTE UFFICIALI, SONO IL FRUTTO DI CONTRIBUZIONE DA PARTE DEGLI STUDENTI E NON SONO STATE ESAMINATE DAL DOCENTE => CAVEAT EMPTOR

  

* **definizione di sistema embedded**

Un Sistema Embedded è l'insieme composto da hw e sw (firmware ovvero sw direttamente integrato in un componente elettronico) dedicato a specifici scopi i cui elementi siano integrati e incorporati in un altro apparato più grande.

  

* **panoramica generale sui sistemi embedded, classi di device, caratteristiche, ordini di grandezza (dimensioni, potenze, consumi, ecc.), ambiti di utilizzo**

Alcuni settori di utilizzo dei sistemi embedded sono:

- POS e bancomat
- stampanti e fotocopiatrici
- elettrodomestici
- router e switch
- smart TV, telefoni ect
- IoT (Internet of Things)

Si tratta di dispositivi con una potenza computazionale ridotta se paragonata a PC o simili.

  

Generalmente hanno buoni consumi energetici e dimensioni compatte. Infatti di per sé non producono abbastanza energia per alimentare attuatori esterni (ma possono attuare degli apparati che fanno funzioare apparati più grossi. Esempio: esp8266 un pollice di grandezza, in ingresso accettano 3.3V/5V, in uscita dai singoli gpio 20/30 milliAmpere (in totale non più di 50/60 milliAmpere).

  

La potenza computazionale di un sistema embedded è un fattore discriminante per identificare le varie categorie sulla base dell’architettura hardware necessaria. È possibile infatti fornire una prima suddivisione sulla base del tipo di elaboratore utilizzato in tre macro-gruppi:

- PLC (Programmable Logic Controller)

- Microcontrollori

- SoC (System-on-Chip)

  

* **componenti interni di un MCU**

un microcontrollore o MCU (MicroController Unit) consiste in un sistema hardware completo in un singolo chip. Hanno una potenza di calcolo limitata (dai 200Mhz in giù, spesso sotto i 100), ottimi consumi energetici (meno di 1W) e ottima efficienza termica. Può contenere:

- Unità di elaborazione

- memoria dati (RAM o EPROM)

- oscillatore

- Memoria programma (ROM, EPROM, FLASH)

- GPIO (General Prurpose Input Output)

- porte di comunicazione base (USART, I2S, SPI, I2C, USB),

- porte di comunicazione analogiche (DAC, ADC, PWM).

- Nei modelli avanzati anche Wifi, Touch Screen, ecc.

  

* **descrivere PLC**

I PLC (Programmable Logic Controller) sono dispositivi relativamente semplici, progettati per sistemi di automazione e programmati per eseguire funzioni specifiche (per questo non sono prodotti su larga scala). È dotato di una buona connettività input/output per interagire con vari sensori ed attuatori. Sono programmabili con 4 linguaggi:

- 2 testuali

- ST (Structured Text, simile al Pascal)

- IL (Instruction List, simile all'assembly)

- 2 grafici:

- FBD (Function Block Diagram)

- LD (Ladder Diagram)

Per quanto i vari prodotti condividano i concetti base di programmazione dei PLC, tali prodotti non sono interscambiabili o compatibili tra loro.

  

* **definire SoC, cosa contiene, come si "combina" per la realizzazione dei vari prodotti reali**

un SoC (System On Chip) è una singola unità che può contenere quasi tutte le componenti del sistema con più potenza computazionale, rispetto a PLC e MCU.

Può contenere: CPU, GPU, ISP (Image Signal Processor), Decoder/Encoder video, WiFi, Bluetooth, Display controller, Audio Controller, seriali, USB, ADC/DAC, Sensori, GPS, Modem, RAM, FLASH, ecc. ... È improbabile trovarli tutti in un singolo SoC, tendenzialmente si trova un sottoinsieme.

  

Sono usati praticamente ovunque: automotive, militare, domotica, Set Top Box (lettori multimediali, sistemi tipo chrome cast ecc), navigatori satellitari e telefonia mobile. Al giorno d'oggi la differenza tra SoC e MCU si è fatta più sottile.

  
  

## Concetti: tutto, in dettaglio.

  

* **sistemi monoprogrammati e multiprogrammati, differenze, caratteristiche, cosa c'entra la MdT?**

In un sistema monoprogrammato viene eseguito un solo programma alla volta senza parallelismi (un solo thread) mentre in un sistema multiprogrammato si possono eseguire più programmi "contemporaneamente" (o con il time sharing).

È possibile effettuare un paragone con la Macchina di Turing (MdT) considerando, il caso dei sistemi monoprogrammati una singola macchina a stati (unità di calcolo) che interpreta i simboli (istruzioni) su un singolo nastro (programma), mentre nel caso dei sistemi multiprogrammati più MdT che lavorano in contemporanea o una che interpreta un simbolo alla volta su più nastri (programmi) diversi.

  

* **conversione AD e DA, caratteristiche, pregi e difetti, considerazioni sul flusso di dati campionati**

La conversione AD (Analogico-Digitale) trasforma un segnale analogico che varia nel tempo in un uno digitale, effettuando una serie discreta di misurazioni, mentre la conversione DA fa l'inverso tramite dei generatori di tensione. Il **campionamento** è il processo con il quale stabilisco ogni quanto effettuare la misurazione.

- La **frequenza di campionamento** è la velocità con cui si fanno le misurazioni (*numero_letture/tempo*)

- il **tempo di campionamento** è il tempo tra le misurazioni.

  

Se un evento dura meno del tempo di campionamento può non essere percepito, mentre uno che dura più della metà del tempo di campionamento rischia di produrre errori perché più segnali potrebbero sovrapporsi (es. [ruota auto](https://web.archive.org/web/20220702080825/https://michaelbach.de/ot/mot-wagonWheel/))

[Teorema Nyquist-Shannon](https://web.archive.org/web/20220830075514/https://fisicisenzapalestra.com/perche-in-accelerazione-le-ruote-girano-al-contrario.html): La frequenza di campionamento dev'essere pari o superiore al doppio della frequenza massima del segnale

  

* **spiegare tecniche di multiplexing (divisione tempo, frequenza), shift register**

Per Multiplexing si intende condividere un canale per trasportare più flussi informativi contemporaneamente. Tecniche:

- **Divisione di frequenza**: I segnali usano frequenze diverse e il ricevente si sintonizza su quella desiderata (es. frequenze telefoni, radio). Se sono troppo vicine c'è interferenza.

- **Divisioni dei tempo**: i segnali vengono inviati sul canale in alternata, il ricevente (de-multiplexer) smista i segnali (es. avvisi con altoparlanti, i messaggi sono letti in sequenza preceduti dal nome).

[Shift register](https://www.logicaprogrammabile.it/shift-register-arduino-74595/): componente esterno che permette di aumentare le uscite es. SN74LS595. Per farlo bisogna necessita ad un pin che faccia da clock, uno che abiliti o meno la scrittura e un'altro per il dato il quale determini quali pin di uscita mettere a 1 o meno.

  

il prezzo che si paga per avere più flussi informativi attraverso un solo canale è la maggiore complicazione lato software.

  

* **differenza fra controllo a loop chiuso e aperto, problemi del loop aperto**

|Open loop|Closed loop|

|:---:|:---:|

|![openloop](https://gitlab.di.unimi.it/sistemiembedded/DomandeEsame/-/raw/master/img/open_loop.jpg?ref_type=heads)|![closedloop](https://gitlab.di.unimi.it/sistemiembedded/DomandeEsame/-/raw/master/img/closed_loop.jpg?ref_type=heads)|

  

Modello per rappresentare il funzionamento del sistema: f(C(t),A(t),U(t)).

  

per **controllo a loop chiuso** ( f(C(t),A(t),U(t)) ) intendiamo un sistema la cui variazione di stato nel tempo dipende dalle variabili di ingresso(C), dalle variabili ambientali(A) (es. umidità) e dalle variabili di uscita precedenti(U). (Esempio PIR: variazione di calore perciò deve conoscere la rilevazione precedente)

  

per **controllo a loop aperto** ( f(C(t),A(t)) ) intendiamo un sistema la cui variazione di stato nel tempo dipende solo dalle variabili di ingresso e da quelle ambientali (Esempio: LED).

Il problema del controllo a loop aperto è che non c'è nessun controllo dell'efficacia dell'azione. (es. con motore step non siamo sicuri che mantenga una velocità stabilita poiché se aggiungessimo un carico, questa rallenterebbe a fronte di un input invariato)

  

* **spiegare tecnica PID per controllo a loop chiuso**

Per PID si intende Proporzionale-Integrativa-Derivativa ovvero:

- **Proporzionale**: la distanza assoluta dallo stato desiderato utilizzando lo stato attuale per valutare quanto sia distante dall'obiettivo.

- **Integrativa**: la storia dell'evoluzione dello stato del sistema calcolata in una finestra temporale (es.media dell'errore).

- **Derivativa**: la velocità di variazione dello stato dall'obiettivo.

Una volta calcolati i valori vanno stabiliti dei coefficienti per pesare la funzione P*(distanza) + I*(media errore) + D*(velocità variazione - può corrispondere alla distanza). È importate avere una funzione che definisca l'errore. Nel caso del motore e(t)= RegimeDesiderato - GiriMotore

esempio:

Ipotizzando che vogliamo un motore che vada ad un regime di 1400 giri

  

|Istante|Regime|Errore|

|:--:|:--:|:--:|

|t-3:|1170|230|

|t-2:|1200|200|

|t-1:|1250|150|

|t:|1300|100|

  

P: (1400 − 1300) = 100

I: (230 + 200 + 150 + 100)/4 = 170

D: (1400 − 1300) = 100

pesando P=I=D=0.5 otteniamo 0.5*100 + 0.5*170 + 0.5*100 = 50+85+50 = 185

  

Potremmo usare 185 come valore da aggiungere alla tensione data al motore.

Calcoliamo cosa accadrebbe ora al tempo t+1 dopo la modifica e nel caso aggiustiamo i pesi attribuiti a P,I,D.

Se mal calcolata si rischierebbe di non raggiungere mai l'obiettivo (se correzione troppo debole) o oscillare intorno all'obiettivo (se correzione troppo forte).

  

* **considerazioni sull'uso della memoria in un Arduino, rispetto ai tipi di dati disponibili**

Essendo la memoria di Ardinuo (e in generale dei dispositivi embedded) molto limitata (intorno ai 2 KB) è bene gestire con cura le tipologie di variabili dichiarate.

Es:

Se necessito di un numero che va da 1 a 10 è inutile dichiarare una variabile di tipo long(4B) e neanche un int(2B), ma basterebbe un byte(1B # da 0 a 255) o un char(1B).

Dato che anche i record di attivazione delle chiamate di funzioni occupano stack, è utile cercare di ridurle evitando lo stack overflow (usando la ricorsione si fa molto uso di chiamate di funzioni).

Se si usano diverse stringhe preformate si può ridurre l'uso della RAM usando la funzione F() per leggere direttamente dalla Flash le stringhe.

Anziché scrivere;

```c

Serial.print("Stringa");

```

Si scriverà:

```c

Serial.print(F("Stringa"))

```

Ciò vale per qualsiasi stringa predefinita.

La stringa verrà presa direttamente dalla flash quando necessaria anziché ricopiarla prima in RAM.

  

Inoltre bisogna anche notare che i sistemi embedded spesso non dispongono di una MMU (Memory Management Unit), il che significa che non c'è protezione della memoria né gestione della memoria virtuale. Di conseguenza, tutti gli accessi alla memoria devono essere gestiti dal programmatore per evitare accessi non controllati, come il superamento degli indici di un array o lo sforamento dello stack/heap, che possono avere effetti catastrofici.

  

* **architettura Von Neumann vs. Harvard**

L'architettura di Von Neumann è quella presente negli attuali pc. Questa consiste in una Macchina di Turing in cui il nastro è unico e contiene sia dati che programma. L'architettura Harvard, invece, è una MdT in cui i nastri rappresentanti la memoria dati e programma sono separati (es. Arduino)

  

* **argomentare validità della ricorsione in ambito embedded, vantaggi e svantaggi**

L'uso della ricorsione permette spesso di scrivere codice più leggibile e semplice, ma il record di attivazione delle chiamate di funzione occupa molto spazio nello stack. L'ambito dei sistemi embedded è costellato da architetture con poca memoria ram pertanto le chiamate ricorsive potrebbero portare ad uno stack overflow potenzialmente non segnalato, portando effetti poco prevedibili.

  

* **descrivere la gestione della memoria in un sistema embedded**

Nella maggior parte non è presente l'MMU (Memory Management Unit), pertanto gli accessi a memoria non sono controllati e la loro gestione è demandata allo sviluppatore. Se l'indice di lettura/scrittura di un array sfora la sua size, si leggeranno o scriveranno altre locazioni di memoria. Stessa cosa per uno stack overflow, non si avranno messaggi di errore, ma si scriverà su altre locazioni.

  

* **spiegare meccanismo dell'interrupt**

Permette l’attivazione di una “azione” (es. invocazione di funzione) in corrispondenza di un “avvenimento” (segnale su un pin).

- ISR (Interrupt Service Routine), è la funzione. deve essere void e senza parametri.

- attachInterrupt(), "aggancia" la funzione a uno o più interrupt (il segnale può essere LOW, HIGH, CHANGE, RISING, FALLING)

Nel caso in cui si verifichi l'evento definito su quel pin () viene sospesa l'esecuzione del loop ed eseguita la funzione designata.

gestione interrupt su Arduino:

- aggancia una funzione ISR ad un segnale

```c

attachInterrupt(digitalPinToInterrupt(pin), ISR, mode)

```

- sgancia una funzione ISR

```c

detachInterrupt(...)

```

- disabilita gli interrupt (per sezioni critiche)

```c

noInterrupts()

```

- abilita gli interrupt

```c

interrupts()

```

  

* **definire categorie "real time"**

sistemi HW e SW capaci di fornire una risposta in un determinato tempo o in un tempo deterministico (caratteristica non legata necessariamente alla potenza computazionale). Si dividono in:

- **hard real time**: il mancato rispetto di una deadline corrisponde al fallimento totale del sistema (es. ABS della macchina).

- **soft real time**: il sistema degrada (di prestazioni o di qualità del servizio)all'aumentare delle tempistiche non rispettate, ma non fallisce (es. sistema di comunicazione vocale).

- **firm real time**: il sistema può tollerare un numero molto limitato di mancate deadline, ma fallisce in caso superino un certo limite.

  

HW e SW sono progettati appositamente per lo scopo e mirando a garantire innanzi tutto l'affidabilità. impiegati in ambienti critici che richiedono processi avanzati di verifica e certificazione.

Si utilizzano sistemi operativi RTOS (Real-Time Operating Systems) che hanno codice più compatto, con meno funzioni rispetto ai sistemi operativi per Desktop/Workstation, e sono ottimizzati per compiti specifici.

  

* **spiegare licenza proprietaria vs. libera**

**licenza proprietaria**: Si tratta di sistemi per i quali ogni versione del software deve essere distribuita secondo i termini di una EULA (End User License Agreement), generalmente associata a un costo economico. La distribuzione, lo sviluppo o la redistribuzione di tali sistemi operativi è possibile solo tramite accordi specifici con il produttore (es Microsoft Windows). Punti chiave:

- divieto di esecuzione su più dispositivi

- divieto di rivendere il programma

- divieto di analisi del codice (reverse engineering)

- divieto di studiarne le prestazioni e pubblicare confronti

- divieto di modifica

- divieto di esportazioni

- divieto di fare copie di sicurezza (non per la legislazione italiana)

- possibile scadenza a termine

**licenza libera**: Si tratta di sistemi operativi di cui sono disponibili i codici sorgente e l’uso per ogni scopo. La tipologia di licenza consente di sviluppare e rilasciare le proprie copie del prodotto sviluppato (es. sistemi GNU/Linux rilasciati sotto licenza GPL). Punti chiave:

- L0: libertà di esecuzione per qualsiasi scopo

- L1: libertà di studiarne il funzionamento e apportare modifiche (accesso al codice sorgente necessario)

- L2: libertà di ridistribuire copie

- L3: libertà di migliorare il programma e pubblicare il codice con i miglioramenti. La comunità ne trae beneficio (accesso al codice sorgente necessario)

  

* **fare esempio di licenza software libera, descrivendone le caratteristiche salienti**

GNU GPL secondo la quale ogni utente deve avere diritto a quattro libertà:

- la libertà di usare il software per qualunque scopo

- la libertà di modificare il software per adattarlo ai propri bisogni,

- la libertà di condividere il software con gli amici e i vicini, ect

- la libertà di condividere le modifiche effettuate.

  

* **descrivere il concetto di watchdog**

si tratta di un sistema di temporizzazione hardware che permette alla CPU la rilevazione di un loop infinito di programma o di una situazione di deadlock (il processore non fa niente per troppo tempo). Quando accade il sistema si resetta in automatico.

  
  

## Richiami: tutto, in dettaglio.

  

* **cos'è la tensione?**

la tensione o potenziale elettrico è la forza di attrazione applicata allo spostamento degli elettroni tra due poli. Si misura in **Volt**.

  

* **cos'è l'intensità?**

l'intensità è la quantità di elettroni (Coulomb) spostati in un secondo. Si misura in **Ampere**.

  

* **descrivere a grandi linee il funzionamento di un resistore/condensatore/transistor/etc./... citare utilizzi**

- **interruttore**: apertura/chiusura di un circuito azionato a mano (il pulstante è un interruttore con molla di ritorno alla posizione iniziale)

- **relè interrutore/deviatore**: pulsante comandato da un elettromagnete. Si usa per comandare flussi elettrici importati (in intensità o tensione) usando flussi meno importanti. Garantisce l'isolamento elettrico tra il circuito di controllo e i contatti di uscita (nucleo ferromagnetico avvolto in una bobina di filo elettrico. Se passa corrente nella bobina, il nucleo diventa magnetico e cambia lo stato).

- **resistenza (o resistore)**: riduce la tensione di un flusso di corrente che la attraversa dissipando la potenza in calore. Utilizzata per:

- generare calore (phone) negli elettrodomestici

- per ridurre la tensione $V=R*I$ (es. partitori di tensione)

- per limitare la corrente massima applicata ad un circuito $I=\frac{V}{R}$

- **condensatore**: permette l'accumulo temporaneo di elettroni. Formato da due piastre conduttive vicine separate da un materiale più isolante dell'aria. Si carica applicandogli una tensione e si scarica applicandovi un carico. la velocità di scarica diminuisce nel tempo poiché nel mentre diminuisce anche la tensione.

- **semi-conduttori**: conducono o meno corrente (grazie a dei cristalli a base silicio) in base a varie condizioni di contorno (come temperatura,luce, ecc.).

- **diodo**: particolare semi-conduttore che fa passare la corrente in un unica direzione. Dando tensione positiva all'anodo la corrente scorre, altrimenti è come un interruttore aperto. Il led (Light Emitting Diode) è un tipo di diodo che come caratteristica secondaria emette luce.

- **transistor**: un semiconduttore che si comporta come un relè. Una piccola quantità di corrente definisce il passaggio tra due punti dove passa maggior corrente. Se quella di pilotaggio varia nel tempo la corrente in uscita avrà la stessa forma d'onda, ma con intensità maggiore. Esistono transistor che anziché usare flussi di corrente per pilotare usano campi elettrici diminuendo la dispersione di calore. I transistor hanno il vantaggio (al contrario dei relè) di non avere parti meccaniche in movimento

  

* **panoramica delle unità di misura (elettricità/elettronica) e loro significato**

- **Volt**: associato alla tensione

- **Ampere**: associato all'intensità (corrente)

- **Ohm**: associato alle resistenze

- **Watt**: associato alla potenza

- **Hertz**: associato ad un segnale sinusoidale indica quanti cicli completi (da picco a picco) vengono effettuati in un secondo (es. 100 Hz sono 100 cicli in un secondo)

  

* **spiegare i collegamenti serie e parallelo per resistori e condensatori**

resistenze:

- **in serie**: si sommano

- **in parallelo**: seguono la formula $R_{tot}=\frac{R_1*R_2}{R_1+R_2}$. Il flusso di corrente si distribuisce proporzionalmente al valore delle resistenze

  

condensatori:

- **in serie**: la capacità totale si comporta come le resistenze in parallelo $C_{tot}=\frac{C_1*C_2}{C_1+C_2}$

- **in parallelo** la capacità totale è data dalla sommo dai componenti

  

* **descrivere un filtro passa alto/basso, elencare utilizzi**

sono dei circuiti RC (resistenza-condensatore) i quali nella loro forma più semplice sono composti da una sola resistenza e da un solo condensatore accoppiati in serie/parallelo.

Se all'ingresso vengono iniettati segnali sinusoidali, all'uscita si avranno segnali con la stessa forma d'onda ma con diversi gradi di attenuazione in funzione della frequenza, da cui i nomi di:

- **"passo-basso"** o "integratore", fa passare, cioè non attenua, i segnali ad alta frequenza

- **"passo-alto"** o "differenziatore", fa l'opposto

  

* **spiegare Veff (efficace)**

$V_{eff}=\frac{V_{picco}}{\sqrt{2}}$ Indica il valore equivalente della tensione alternata che produrrebbe la stessa potenza dissipata, in un resistore, di una tensione continua (DC) di uguale valore.

  

* **descrivere leggi di Kirchhoff**

- **delle correnti**: in un nodo (giunzione di più percorsi del circuito) la somma delle correnti entranti e quelle uscenti si bilanciano. Quindi non si creano o perdono elettroni.

$\sum_{k archi}I_k=0$

- **delle tensioni**: in un circuito, la somma delle tensioni è pari a 0. Quindi non si creano o perdono differenze di potenziale.

$\sum_{k tratti}V_k=0$

  

* **differenza fra corrente alternata e continua**

la differenza è nel comportamento degli elettroni, nella continua si muovono in una direzione, nella alternata cambiano verso con una frequenza (Hertz). Altre differenze:

- **produzione**: alternata meccanicamente o elettronicamente (inverter), continua chimicamente, per accumulo elettrostatico o meccanica (dinamo)

- **immagazzinamento**: alternata non accumulabile senza trasformarla in altra energia (dighe), continua accumulatori chimici (batterie), condensatori

- **trasformabilità**: alternata facilmente trasformabile con un **trasformatore**, continua non facilmente trasformabile

- **trasportabilità**: la corrente alternata semplifica la trasportabilità e con le leggi di Ohm capiamo che aiuta alzare la tensione a scapito dell'intensità per portare più potenza senza disperdere troppo calore.

$P=V*I$ e $P=R*I^2$

  

* **cos'è la potenza elettrica?**

la potenza è la capacità di produrre lavoro.

  

* **cos'è un segnale?**

un segnale elettrico è un informazione associata a grandezze di tensione e corrente su conduttori.

  

* **quale effetto ha un condensatore su un segnale variabile?**

le armature si caricano e si scaricano in continuazione per induzione elettrostatica generando ai suoi capi una corrente variabile

  

* **cosa si intende con "forma d'onda"?**

La forma d'onda è una rappresentazione cartesiana di una grandezza elettrica (Tensione o corrente) rispetto al tempo

  

* **spiegare costante di tempo RC**

tempo impiegato dal condensatore per caricare il 63,2% della capacità restante da caricare.

$t=R*C$ (R è la resistenza in Ohm, C è la capacità in farad)

(esempio un condensatore scarico impiegherà t tempo per caricare il 63,2% della sua capacità totale, un altro t tempo per caricare il 63,2% del rimanente e così via per avvicinamenti successivi fino al limite del 100%

  

* **descrivere integratore (passa basso) e differenziatore (passa alto) RC**

prendono questi nomi quando ai filtri passa alto/basso si fornisce in ingresso una tensione variabile nel tempo di forma quadra. Nel caso dell’integratore il segnale di uscita assumerà la forma del “dente di sega”, mentre nel caso del differenziatore si otterrà un "treno di impulsi"

  

* **descrivere leggi di Ohm e loro significato**

- $I=\frac{V}{R}$: indica che l'intensità è direttamente proporzionale alla tensione e inversamente alla resistenza.

- $P=R*I^2$: indica che la potenza (intesa anche come calore dissipato) e misurata in Watt, è proporzionale alla resistenza per il quadrato dell'intensità (Perciò ridurre l'intensità ha un effetto maggiore sulla riduzione del calore dissipato)

- Dalle prime due si può derivare $P=V*I$

  

* **panoramica generale su sensori "fisici", esempi**

un oggetto basato su un materiale che cambia le sue proprietà elettriche al variare delle condizioni ambientali a cui è sottoposto.

es:

- **fotoresistenza**: varia la sua resistenza interna al variare della luce che la colpisce

- **sensore di rumore a condensatore**: una delle due piastre del condensatore è strutturata in modo da muoversi quando colpita da onde sonore e, quindi, si ottiene che in caso di rumore cambia la capacità del condensatore.

- **interruttore a mercurio**: bulbo di vetro contenete una goccia di mercurio al suo interno e due elettrodi. Muovendo il bulbo si muove la goccia che, in base a come è orientato il bulbo, potrebbe chiudere il contatto elettrico degli elettrodi. Si ottiene così un sensore di pendenza fisico

  

* **panoramica generale su sensori "numerici", esempi**

Sensori più complessi che forniscono un output numerico.

es:

- sensore di distanza a ultrasuoni: un mini-buzzer (emettitore di suono) emette ultrasuoni e un mini-microfono li cattura. Il tempo tra l'emissione e la ricezione aiuta a stabilire la presenza di ostacoli (riflettenti) e la loro distanza.

  

* **panoramica generale su attuatori, esempi**

Un attuatore è un dispositivo che cambia le proprie proprietà meccanica in funzione di segnali elettrici in input.

es:

- motori

- relè

  

* **panoramica generale su motori, esempi**

- **motore a corrente continua**: passa da statico a in movimento in base alla tensione o corrente applicata.

- **servomotori e stepper (motori passo-passo)**: posizionano il loro asse a un angolo preciso in funzione del segnale di ingresso.

  

* **panoramica strumenti di misura e loro uso, problemi possibili**

- **lampadina attaccata a coppia di fili collegati a dei morsetti**: si collega un morsetto a masse e l'altro lo si attacca nelle varie parti del circuito. Se arriva tensione la lampadina si accenderà. la lampadina deve essere scelta in modo che possa accendersi alla tensione desiderata.

Nell'ambito embedded si usa il led anziché la lampadina, nel caso munito di resistenze se la tensione è troppo alta.

Se la lampadina è collegata in serie ad una batteria allora la si può usare per testare la continuità. es. su un cavi interrato, senza dissotterrarlo, cortocircuito i capi inserendoci in mezzo il "tester". Se la lampadina si accende il cavo è a posto.

- **voltmetro**: strumento che misura la tensione tra di punti di un circuito. Lavora in parallelo. Serve a capire se ci sono parti insufficientemente alimentate o non alimentate.

- **amperometro**: strumento che si inserisce in serie e misura l'intensità di corrente passante. Serve per misurare l'intensità, stimare il consumo e per valutare la potenza impiegata con la legge di Ohm $P=R*I^2$. Ha resistenza bassissima per interferire il meno possibile con le misurazioni. Se collegato ad una funte di alimentazione saltano le protezioni (se le ha) o si fondono i cavi,

- **pinza amperometrica**: tipo di amperometro usabile in parallelo. Le due ganasce della pinza si chiudono su un filo e misurano per induzione elettromagnetica il campo elettromagnetico.

- **ohmometro**: misura i valori di resistenza e lo si può usare per valutare la condizione di una giunzione (diodi e transistor):

- giunzione interrotta: resistenza infinita in entrambi i sensi

- giunzione in corto: resistenza zero in entrambi i sensi

- giunzione possibilmente a posto: resistenza infinita in un senso e zero nell'altro

è uno strumento attivo composto da un amperometro e una pila che fornisce tensione. Viene immessa la tensione di regime al componente da valutare e misurando la corrente (intensità) che scorre nel circuito e usato la legge di Ohm $R_{incognita}=\frac{V_{immessa}}{I_{misurata}}$

- **multimetro**: strumento che integra i vari strumenti di misura.

- **oscilloscopio**: misura le forme d'onda. se collegato a due punti di un circuito visualizza su un display il grafico dell'andamento della tensione. Solitamente hanno più ingressi per poter confrontare più forme d'onda contemporaneamente.

  

* **spiegare PWM e utilizzi**

Un Pulse With Modulation è un segnale con una forma d'onda quadrata con un periodo fisso ma non simmetrico (tra alto e basso). la modulazione dell'onda avviene variando la durata dell'impulso alto, misurata in percentuale come **duty cycle** (es. un duty 50% = pwm simmetrica, un duty al 10% = il segnale è alto per 1/10 del periodo).

Solitamente la semi-onda alta corrisponde all'1 logico e quella bassa 0 logico.

Usi:

- passaggio di informazioni allungando o diminuendo la durata del segnale alto rispetto a quello basso (es. telegrafo). L'attrezzo che misura il segnale ne determina la semantica.

- sfrutta l'inerzia di carichi come motori elettrici e lampadine a filamento per regolarne la velocità o intensità.Un motore continua a girare per inerzia quando l'alimentazione è interrotta. In questo modo si può regolare manualmente la velocità del motore, ottenendo una riduzione costante.

  

## Architetture: tutto, in dettaglio.

  

* **cos'è un ISA?**

Per definire un'architettura è essenziale conoscere il suo modello astratto, denominato Instruction Set Architecture (ISA). Questo modello include la tipologia di dati trattabili, i registri, la modellazione di input/output e le istruzioni macchina.

da un singolo ISA possono derivare diverse implementazioni (processori anche di anni diversi possono condividere lo stesso ISA).

  
  

* **differenze fra CISC, RISC, VLIW, EPIC**

- **CISC** (Complex Istruction Set Computing): architetture con tante istruzioni low-level di dimensione variabile che possono richiedere diversi cicli di clock per essere completate. Le istruzioni possono avvicinarsi a quelle di alto livello, ma la complessità circuitale ne aumenta i costi di realizzazione (servono più componenti).

- **RISC** (Reduced Istruction Set Computing): architettura con poche, semplici e ottimizzate istruzioni completabili in pochi cicli di clock. Basso costo in silicio, grande efficienza, ma difficoltà di programmazione per il basso livello. È fondamentale avere compilatori efficienti.

- **VLIW** (Very Long Instruction Word):

- **EPIC** (Explicitly Parallel Instruction Computing)

VLIW e EPIC sono studiati per la parallelizzazione (non servono per il corso).

  

* **esempi CISC e RISC**

**CISC**: Intel 8080, x86 (in realtà aveva una sezione interna che traduceva le istruzioni CISC in microistruzioni simili alle RISC)

**RISC**: ARM, MIPS

  

* **cosa si intende con "endianness"?**

Si intende l'ordine di memorizzazione dei byte nella memoria.

- **Little Endian**: I byte sono memorizzati a partire dal byte MENO significativo (più popolare) (es. 0x AB CD -> CD AB)

- **Big Endian**: I byte sono memorizzati a partire dal byte PIÙ significativo (es. 0x AB CD -> AB CD)

  

* **cos'è un FPGA?**

Un FPGA (Field-Programmable Gate Array) è un insieme di blocchi formati, a loro volta da insiemi di porte logiche (es. flip-flop) raggruppati in base alla funzionalità necessarie e sono programmabili tramite appositi "linguaggi". Sono molto più costosi di MCU o SoC, e solitamente vengono utilizzati per la costruzione di prototipi e in fase di progettazione.

  

* **descrivere architettura AVR con esempi**

Le MCU AVR sono state le prime ad utilizzare una memoria Flash On-Chip anziché ROM/EEPROM esterne. Sono utilizzate nelle applicazioni embedded a bassa richiesta computazionale, Sono diventate più popolari con la nascita di Arduino che le implementava (casa madre delle AVR: **Atmel**). L'architettura AVR32 è stata progetta per entrare in competizione con ARM per gli embedded di fascia media.

  

* **descrivere architettura Xtensa con esempi**

microcontrollore RISC ad elevate prestazioni con bassi consumi. L'architettura puntava sulla flessibilità ed estensibilità e l'isa, nonostante a 32 bit, era capace di eseguire istruzioni a 16 o 24 bit riducendo così le dimensioni del codice.

  

* **cosa si intende con SoC/demo board/eval board/validation board?**

- **evaluation board** (o demo board): un PCB con il chip di riferimento e i collegamenti fisici per ad altri dispositivi HW (bus, video, rete, video, JTAG(debug)) al fine di mostrare le sue potenzialità. (es. RaspberryPI ha avuto successo tramite la sua eval board) Il tutto facilita anche lo sviluppo di HW e SW basato su quel chip.

- **validation board**: board di grandi dimensioni con lo scopo di effettuare "silicon validation" ovvero una verifica per evidenziare errori di progettazione o di strutturazione del chip.

  

* **storia e architettura Arduino**

Arduino nasce in Italia come dispositivo a basso costo a scopo didattico. I progetti hardware sono stati rilasciati in modalità open e sul mercato sono approdati molti kit per la personalizzazione. Arduino è diventato molto noto nel mercato amatoriale. Oltre al dispositivo è stato creato l'IDE che rendeva molto semplice l'upload degli sketch.

  

* **descrivere piattaforma STM32**

MCU con architetture semplici, facilmente personalizzabili e con la possibilità di lavorare facilmente con sistemi senza OS. Sono utilizzate in campi dove è richiesto di superare rigidi protocolli di certificazione come l'ambito medico, automotive e militare.

  

* **descrivere piattaforma ESP8266/ESP32**

SoC con un rapporto prestazioni/prezzo ottimo. È dotato di WiFi on board. Utilizzato estensivamente nell'ambito amatoriale e in quello professionale.

  

* **cos'è NodeMCU?**

Firmware da caricare sull'ESP8266 per poter effettuare l'esecuzione anche interattiva di script LUA. LUA è un linguaggio interpretato leggero ed efficiente che supporta paradigmi procedurali, ad oggetti e funzionali. È dinamicamente tipicizzato e ha un garbage collector.

  

* **cosa si intende con PCB?**

Il PCB "Printed Circuit Board" è il circuito stampato. Solitamente è uno strato di rame ricoperto dove vengono incise le piste per le connessioni dei vari componenti.

  
  

## Mem e I/O: tutto, in dettaglio.

  

* **differenze fra i vari tipi di memoria (RAM/ROM/flash/EPROM/sequenziale/casuale/SDRAM/DRAM/DDR/etc.)**

- **RAM** (Random Access Memory): memoria ad accesso casuale. Tipicamente voltatile, stesso tempo per accedere a qualsiasi porzione memoria, costo alto.

- **SRAM** (Static RAM): Memorie RAM che non necessitano di refresh del dato. Molto veloce, molto costosa, ottime prestazioni energetiche e termiche. Usata solitamente nelle cache.

- **DRAM** (Dynsmic RAM): Memorie RAM che necessitano di refresh del dato non necessariamente sincronizzate con il clock del sistema. Meno costose ed economiche delle SRAM.

- **SDRAM** (Syncronus Dynamic RAM): DRAM sincronizzate con il clock del sistema.

- **DDR** (Double Data Rate): tipo di SDRAM.

- **Memoria ad accesso diretto**: Non volatile, lenta, costo più basso. Usata per le memoria di massa.

- **ROM** (Read Only Memory): Nate come memorie non riscrivibili. I dati venivano codificati direttamente su silicio. Si sono poi evolute integrando la possibilità di riscrittura.

- **PROM** (Programmable Read-Only Memory): memorie programmabili una sola volta tramite corrente ad alto potenziale (da qui *burn the ROM*)

- **EPROM** (Erasable PROM): memorie riscrivibili un numero limitato di volte (~1000). La programmazione avviene dopo aver azzerato i dati tramite l'esposizione a luce ultravioletta.

- **EEPROM** (Electrically Erasable PROM): memorie cancellabili e riscrivibili elettricamente un numero limitato di volte. (Veloce in lettura, ma molto lenta in scrittura) Usata solitamente in fase di bootstrap e per funzioni di base del sistema.

- **Flah Memory**: deriva dalle EEPROM ma ha la capacità di essere cancellata e riscritta a blocchi o unità inferiori e non interamente. Un blocco può essere riscritto un numero limitato di volte. In base al tipo di collegamento tra le celle si dividono in:

- **NAND Memory**: i transistor sono collegati in modo da collegare in serie le celle. Meno costose e meno spazio su silicio. Struttura a pagine (512-4096 Byte) riunite in blocchi da 32-128 pagine. Usate in dispositivo removibili. (es. chiavette USB, schede SD)

- **NOR Memory**: celle collegate a massa e in parallelo alla bit line (linea di informazione). ogni cella è leggibile e scrivibile singolarmente. Occupa più spazio nelle NAND. Nate come sostituto delle EEPROM mirano ha ottimizzare la lettura (frequente) a scapito della scrittura (rara). Il codice oggetto contenuto nelle memorie NOR può essere eseguito sul posto senza essere caricato su una memoria esterna => ideale per il boot dove la memoria potrebbe non essere accessibile

- **Supporto magnetico**: HDD

- **Supporto ottico**: CD, Blueray, ...

- **Memoria ad accesso sequenziale**: Molto lenta, non costosa. Usata per i sistemi di backup a nastro.

- **Nastro**

  

* **cos'è e cosa fa una MMU?**

L'MMU (Memory Management Unit) è un componente che si occupa della gestione della memoria effettuando:

- traduzione degli indirizzi virtuali in fisici

- protezione della memoria

- gestione della cache

  

* **panoramica supporti memoria di massa nell'embedded, pregi e difetti**

Solitamente vengono utilizzate memorie NAND per lo storage principale e le NOR per le funzioni di basso livello e il boot.

  

* **cosa si intende con XIP? pregi e difetti?**

caratteristica delle memorie NOR. Execute in place (XIP) è un metodo per eseguire programmi direttamente dalla memoria a lungo termine bypassando il bisogno di copiarli nella RAM, lasciandola libera per altri usi. Viene spesso usato come primo bootload nei sistemi con bootload a più fasi o in sistemi con RAM estremamente limitata

In sistemi senza tabella di paginazione l'intero file deve essere immagazzinato in byte consecutivi e non essere frammentato, ma le memorie flash sono spesso programmate per frammentare i dati in modo da consumare uniformemente il chip (wear leveling)

  

* **quali tipi di filesystem vengono usati nell'embedded? pregi e difetti**

Se vengono rimossi i controller che permettono di utilizzare i classici filesystem a blocchi (es. FAT, NTFS, ext) è necessario utilizzare filesystem speciali come:

- jffs: "Log Structured Filesystem" che lavora con le NAND, ma necessita fasi di clean ogni volta che viene montato.

- yaffs: Simile a jffs, utilizzato dai primi produttori Android

- ubifs: ottimizzazioni del "wear level" e minori tempi di accesso in fase di mount.

  

* **cos'è il "wear leveling"?**

Sistema per evitare che venga riscritto sempre lo stesso blocco di memoria ed evitare il suo cessato funzionamento prematuro, utilizzato per prolungare la vita ai supporti di memoria.

  

* **cos'è una RS232? che caratteristiche ha?**

Protocollo standard per la comunicazione seriale. I dati sono trasmessi un bit alla volta e il valore è definito dalla differenza di potenziale rispetto la massa (GND):

- da +3V a +15V bit di valore 0.

- tra -3V e +3V segnale non valido usato per eliminare il rumore (necessità per le cablature e circuiti del passato)

- da -3V a -15V bit di valore 1.

Spesso si usano sistemi a "3 fili" TxD (Trasmitted Data), RxD (Recived Data) e GND.

Oggi i seriali standard sono sostituiti da i seriali TTL che utilizzano valori più bassi di differenza di potenziale. Si collegano all'USB tramite adattatori.

I seriali sono rimasti in ambito embedded e server in quanto il terminale grafico non è sempre necessario o possibile. Nell'ambito desktop sono stati sostituiti dall'USB.

  

* **descrivere NMEA0183**

standard

- sia elettrico: descrive un bus seriale RS-422 => due cavi per TxD e due per RxD risultando insensibile al rumore e arrivando a distanze maggiori

- sia di protocollo: dati trasmessi in ASCII e organizzate in stringhe dove il formato ha significato.

Usato in ambito nautico e per il GPS.

  

* **descrivere I2C**

I2C (Inter-Integrated Circuit) bus seriale per comunicazioni a breve distanza. Solitamente usato all'interno dello stesso sistema.

È un bus "multi-master" dove i nodi possono essere:

- master: genera il serial clock (SCL - attivo-basso) che abilita l'invio di informazione e fa partire la comunicazione.

- slave: riceve il segnale di clock e risponde quando indirizzato dal master.

Processo:

1. Il master abilita il serial clock SCL

2. il master disattiva il passaggio dati SDA per settare la condizione di start (SCL attivo, SDA disattivo)

3. il master specifica l'indirizzo dello slave di destinazione (7 bit) e 1 bit per il tipo di operazione (read/write)

4. il master attende il segnale di ACK dello slave

5. lo slave manda pacchetti da 8 bit seguiti da un segnale di ACK

6. lo slave manda il segnale di fine trasmissione (stop condition) effettuando l'inverso della condizione di start

  

* **descrivere I2S**

I2S (Inter-Integrated circuit Sound) è un bus per il trasporto di dati audio.

linee bus:

- Continuous Serial Clock (SCK): Ad ogni colpo di clock corrisponde un bit di informazione su la linea dati SD

- Word Select (WS): in base al valore selezione il canale (destri/sinistro)

- Serial Data (SD): linea dati multiplexed in base a WS e frequenza di clock

  

* **descrivere SPI**

SPI (Serial Peripheral Interface) è la specifica di un bus per la comunicazione seriale sincrona master/slave e non multi-master.

Linee bus:

- SCLK (Serial CLoK): segnale attivo-alto inviato dal master che controlla lo spostamento dei vit tra master e slave

- MISO (Master Input Slave Output) attivo-alto

- MOSI (Master Output Slave Input) attivo-alto

- CS (Chip Select): seleziona quale slave abilitare per la comunicazione con il master (abilitato/disabilitato molto distante dalla trasmissione)

Quando il clock viene abilitato dal master, vengono trasmessi i dati in seriale.

Solitamente non vi è altra condizione di inizio/fine trasmissione.

  

* **descrivere CAN-BUS**

CAN è uno standard di comunicazione master-slave (può essere anche multi-master) basato sui piccoli messaggi usato nell'ambito automotive e industriale per la sua semplicità di implementazione e alta affidabilità.

1. Ogni nodo deve aspettare un tempo prestabilito per inviare il proprio messaggio

2. Vengono rilevate potenziali collisioni tra i frame e, in base alla priorità degli ID, viene stabilito quale messaggio far arrivare.

Tipi di frame:

- Data Frame: passaggio dati

- Error Frame: inviato dai nodi che ricevono frame malformati

- Overload Frame: inviato dai nodi che necessitano di prendere tempo tra un frame e l'altro

- Remore Frame: inviato per sollecitare l'invio di frame

  

* **descrivere Ethernet**

Standard per le connessione con la presa RJ-45.

Scheda di rete composta da due elementi HW che possono essere forniti da due produttori diversi:

- MAC (Media Access Control): livello 2 della pila ISO/OSI

- PHY (Physical Layer): livello 1 della pila ISO/OSI

Spesso il MAC si trova all'interno del SoC e il PHY all'esterno, sulla board. Ciò consente di poterlo rimuovere dopo le fasi di sviluppo se non si intende utilizzarlo.

  

* **a cosa serve una linea di CLOCK? se ne può fare a meno?**

Può servire per:

- abilitare la trasmissione di dati

- sincronizzare i dispositivi

  

* **vantaggi e svantaggi del "chip select"**

il segnale "Chip Select" offre una soluzione efficiente per gestire la comunicazione con più dispositivi su un singolo bus, ma presenta anche limiti in termini di numero di dispositivi, complessità del cablaggio e utilizzo delle risorse del microcontrollore.

  

* **cosa si intende con GPIO? come viene usato?**

Un GPIO (General Purpose Input/Output) è la rappresentazione di un pin e del suo segnale digitale transitante. L'informazione passata dipende dalle tensione transitate su di esso alta/bassa.

Spesso è possibile scegliere se configurarli tramite software per associarli a qualche Intellectual Property o destinarlo come GPIO.

  

* **pullup e pulldown**

Metodo per non far fluttuare lettura di un GPIO quando è aperto.

Pull-Up: quando si inserisce una resistenza tra il GPIO e l'alimentazione (risulta sempre HIGH mentre aperto).

Pull-Down: quando si inserisce una resistenza tra il GPIO e la massa (risulta sempre LOW mentre aperto).

  

* **cos'è il "bit banging"? vantaggi e svantaggi**

Il bit banging è una tecnica per implementare comunicazioni seriali generando via software treni di impulsi in modo da emulare un circuito apposito.

Bisogna essere sicuri che il ciclo venga eseguito con una velocità nota e stabile altrimenti si rischiano errori di trasmissione.

Vantaggi:

- economico

- flessibile rispetto al protocollo di comunicazione. Basa aggiornamenti software per introdurre nuovi protocolli.

Svantaggi

- minor robustezza: la stabilità è influenzata da cosa viene eseguito sull'hardware. Se arrivano tanti input si rischia di perdere dati.

  

* **perché negli alimentatori switching non riesco a notare le oscillazioni di corrente?**

Perchè sono ad alta frequenza (da Kilo a Mega Hertz)

  

* **cos'è il JTAG?**

Il JTAG (Join Test Action Group) è uno strumento per il testing e la validazione hardware e software di basso livello (es. driver) delle board.

Semplificando è come una linea di celle interconnesse tutte intorno alla logica I/O del chip. Le celle possono raccogliere le informazione sullo stato complessivo di tutti i registri e della memoria permettendo un controllo completo su quello che viene eseguito all'interno dell'elaboratore. Viene gestito tramite connettori JTAG. Sono solitamente rimossi per specifiche di sicurezza e per evitare reverse engineering sulla board di produzione.

  
  

## S.O.: overview

  

* **cos'è un S.O.?**

Il sistema operativo è un elemento software atto a gestire le risorse hardware del sistema e offrire servizi agli altri software.

  

* **descrivere architettura monolitica/microkernel/etc.**

struttura kernel:

- **monolitica**: il nucleo comprende driver, strutture di multiplexing dell'hardware e servizio per la gestione dei processi e della comunicazione (es. linux, freeBSD). Nonostante gli svantaggi in termini di manutenzione, estensione e dimensioni, sono molto diffusi per la facilità di sviluppo e i costi complessivamente più bassi.

- **microkernel**: kernel con il minor codice possibile eseguito in modalità supervisore. Gli altri componenti vengono estratti in moduli (es. driver) comunicano con il nucleo tramite componenti software detti "server".

- Vantaggi: sicurezze e robustezza.

- Svantaggi: complessità di sviluppo e rigidità comportamentale complessiva (es. freeRTOS)

- **ibridi**: combinano elementi del microkernel con componenti non essenziali per migliorare semplicità e prestazioni (es. XNU (MacOS) e WindowsNT di Microsoft).

- **exokernel**: approccio accademico, riduce il kernel al solo multiplexing delle risorse hardware, spostando tutte le operazioni OS in librerie esterne (libOS). Questo permetterebbe, teoricamente, la coesistenza di più libOS sopra lo stesso ExoKernel.

  

* **cosa si intende con "preemptive multitasking"?**

attraverso un meccanismo basato su interrupt, viene sospeso il processo corrente, invocato lo scheduler e sulla base di un diverso livello di priorità, viene eseguito un determinato processo. In questo modo si cerca di garantire a tutti i processi un accesso pesato alle risorse hardware.

  

* **cos'è un filesystem?**

È un software per la gestione dell'organizzazione dei file e il loro accesso.

Composto da:

- strutture dati: per organizzare dati (i blocchi dei file) e metadati

- metodi di accesso: mapping delle chiamate dei processi (es: open(), read(), write(), ...) nelle strutture dati e come sono implementati

  

* **cos'è il "root filesystem"?**

il root filesystem è la partizione del filesystem consente gli elementi necessari al boot del sistema (libc, shell o altro interprete di comandi, altri tool ...).

Viene convenzionalmente montata come primo nodo dell'albero delle cartelle "/".

  

* **cos'è un "init system"?**

Insieme degli strumenti software (incluso il processo init) e le configurazioni che permettono l'avvio di tutti gli applicativi e i demoni del sistema

  

* **cos'è una shell?**

È un software che permette l'interpretazione di comandi definiti in un proprio linguaggio (di "scripting") durante l'esecuzione.

  

* **cos'è e cosa serve un bootloader?**

Programma necessario per avviare il sistema. Carica kernel e parametri d'avvio prelevandoli dallo storage.

Se presenti il BIOS/UEFI (firmware in flash o eeprom) saranno questi ad effettuare parte delle configurazioni (es. clock, rilevamento storage, inizializzazione dispositivi di comunicazione, GPU, ...) semplificando il lavoro del bootloader.

  
  

## Linux: overview

  

* **cos'è una toolchain?**

strumenti per la compilazione del codice sorgente (librerie, linker, compilatore, debugger).

La toolchain è compilata per l'architettura su cui lavora, quindi non sono intercambiabili.

- nativa: compilata da un sistema con la medesima architettura di quella target (comune in ambienti desktop)

- cross-toolchain: compilata da un sistema con una architettura differente produce binari per architetture differenti (comune in ambienti embedded)

  

* **cos'è un build system? citarne qualcuno e descrivere**

L'insieme dei software per effettuare la compilazione dei pacchetti del sistema embedded finale.

es

- Buildroot: per generare OS Linux per dispositivi embedded. Può generare: cross-toolchain, root filesystem, immagini kernel e dei vari bootloader.

- Open embedded: basato su layer contenenti recipes che rappresentano in forma testuale i parametri e le istruzioni che compilare i vari elementi del sistema.

  

* **cosa sono le partizioni? che tipi puoi citare e descrivere?**

- MSDOS Partition Table

- GPT (Guid Partition Table)

- Linux:

pro:

- Implementazione e configurazione semplici con bootloader preimpostato

- Massimizzazione dello spazio per il rootfs, aumentando la quantità di software

- Aggiornamento permanente del rootfs durante l’esecuzione del sistema

contro:

- Complessità di gestione dei file rootfs su sistemi non Linux (Windows/MacOS)

- Maggior deterioramento dei dispositivi flash a causa delle ottimizzazioni per dischi rotazionali dei filesystem ext

- Rischio di perdita di dati o problemi di riavvio in caso di spegnimento improvviso o interruzione di corrente

  

## FreeRTOS: overview

  

* **descrivere cos'è FreeRTOS e come viene utilizzato**

FreeRTOS (Free Real Time Operating System) è un sistema operativo semplice e veloce che ha lo scopo di offrire prestazioni real-time.

Non comprende driver nè API complesse ma solo il necessario per la gestione di thread, task, mutex, semafori e timer.

Un prodotto finale FreeRTOS unisce il codice sorgente dei sistema a quello per il supporto dell MCU relativa e al codice dell'applicazione.

  

* **cos'è un task in FreeRTOS?**

I task sono dei programmi all'interno del programma principali (ricordano i processi). Effettivamente sono funzioni contenenti un loop infinito nel quale sono presenti le istruzioni di funzionamento.

Può essere eseguito un solo task alla volta. Possono avere stati diversi come:

- Running: in esecuzione

- Ready: eseguibile da un momento all'altro

- Suspended: esplicitamente fermato e in attesa di esplicita riattivazioni

- Blocked: fermato e in attesa di un evento

  

* **cos'è e a cosa serve un semaforo?**

Sistema per la gestione della concorrenza.

  
  

## Arduino: tutto, in dettaglio

  

* **origine di Arduino**

La storia di Arduino inizia nel 2003 all'Interaction Design Institute di Ivrea, quando lo studente Hernando Barragán inizia a lavorare su una tesi sotto la supervisione di Massimo Banzi e Casey Reas (co-autore del linguaggio Processing). L'obiettivo era creare un ambiente di sviluppo software e hardware economico, semplice e completo, per permettere agli studenti e ai professionisti dell'interaction design di sperimentare in progetti integrati interattivi. A quell'epoca, il mercato non offriva soluzioni a basso costo e di facile utilizzo: le piattaforme embedded costavano centinaia di dollari e gli ambienti di sviluppo erano spesso proprietari con documentazione complessa.

Da questa idea nacque Arduino, che ha attraversato diverse fasi di industrializzazione. Oggi, Arduino non è solo una semplice board, ma comprende:

- una famiglia di board

- diversi ambienti di sviluppo

- vari linguaggi di programmazione

- un sistema operativo completo per alcune board (OpenWrt sulla YUN)

- uno standard de facto per l'I/O

- una vasta rete di produttori e venditori di hardware compatibile

  

Gran parte del software e dell'hardware nell'ecosistema Arduino è open source, incoraggiando la clonazione, riproduzione, miglioramento e redistribuzione della conoscenza. Con queste caratteristiche, Arduino è diventato lo standard di riferimento per le piattaforme embedded, specialmente nel mondo hobbistico e dei makers.

  

* **pro e contro della piattaforma**

Vantaggi:

- Le licenze menzionate rendono Arduino un ambiente con un bassissimo costo di ingresso economico e con un altissimo livello di community.

- presenta un’architettura KISS (Keep It Simple, Stupid!), sia dal punto di vista hardware che software.

- Il linguaggio di programmazione di Arduino ha una sintassi molto simile a C e Java, con costrutti di base praticamente identici, mentre i costrutti più complessi (oggetti, puntatori, etc.) sono mascherati a meno che non si voglia usarli esplicitamente. È un linguaggio imperativo strutturato.

- presenti molte librerie

  

Svantaggi:

- essendo l'hardware Arduino libero e riproducibile anche con produzioni non ufficiali, si possono incontrare board a basso costo con qualità basse

- presenza di troppo librerie alternative

  

* **spiegare meccanismo di boot di un Arduino (classico: UNO)**

- quando la board viene accesa o a seguito di un reset, il bootloader è la prima cosa che viene eseguita

- si mette in attesa (per millisecondi) sulla porta seriale (usb o tramite i pin RX e TX) per vedere se arriva una sequenza di byte predefenita:

- se la board riceve i byte corretti, risponde con un ACK e l'ide invia il codice dello sketch (in binario) memorizzandoli sulla memoria flash (nella parte successiva al bootloader)

- altrimenti, non scrive nessun codice e il bootloader fa una jump direttamente all’inizio del codice

  
  

* **spiegare il funzionamento di setup() e loop()**

- **setup()**: messe tutte le istruzioni di configurazione iniziale (ad es. l’apertura della seriale, la richiesta di indirizzo IP, etc.) da fare una volta per tutte.

- **loop()**: invece tutte le istruzioni vere e proprie del programma che si vuol produrre. Viene chiamata a ripetizione.

  

* **panoramica tipi di dato**

ATMega

- boolean 1 Byte

- char 1 Byte

- unsigned char 1 Byte

- byte 1 byte

- int 16 bit = 2 Byte

- unsigned int

- word = int

- long 32 bit = 4 Byte

- unsigned long

- short 16 bit = 2 Byte

- float 32 bit = 4 Byte

- double 64 bit = 8 Byte

- array: vettori di variabili dello stesso tipo accessibili tramite la posizione (attenzione all'index overflow non controllato)

- string: array di char

- String (oggetto)

  

* **panoramica operatori**

- aritmetici:

- assegnamento "="

- somma "+"

- sottrazione "-"

- prodotto "*"

- divisione "/"

- modulo "%"

- confronto:

- uguale "=="

- diverso "!="

- minore "<"

- maggiore ">"

- minore 0 uguale "<="

- maggiore o uguale ">="

- booleani:

- and "&&"

- or "||"

- not "!"

- puntatori:

- manipolazione dei bit:

- and bit a bit "&"

- or bit a bit "|"

- xor bit a bit "ˆ"

- not bit a bit "~"

- shift bit a sinistra "«"

- shift bit a destra "»"

- composti:

- incremento "++"

- decremento "--"

- somma "+="

- sottrazione "-="

- prodotto "*="

- divisione "/="

- modulo "%="

- and bit a bit "&="

- or bit a bit "|="

* **spiegare direttive compilatore**

le direttive al precompilatore:

- **#include**: il precompilatore le sostituisce con il reale contenuto del file incluso prima di passare il tutto al compilatore

- **#define**: il precompilatore sostituisce nel codice tutti le variabili definire con il loro reale contenuto

  

* **panoramica costrutti di controllo di flusso**

costrutti di selezione:

- if-else

- switch

  

costrutti di ripetizione:

- for

- while/do-while

  

* **cos'è una funzione?**

È un meccanismo per associare un insieme di istruzioni ad una signature in modo da evitare ripetizioni.

  

* **descrivere il meccanismo di gestione degli interrupt facendo esempi di codice**

si può adibire un pin a segnale di interrupt associato ad una funzione. Nel caso in cui si verifichi l'evento definito su quel pin (es. arduino: LOW, HIGH, CHANGE, RISING, FALLING) viene stoppata l'esecuzione del loop ed eseguita la funzione designata.

```c

attachInterrupt(digitalPinToInterrupt(pin), ISR, mode)

```

Si possono anche definire sezioni critiche iniziando con la disabilitazione degli interrupt con noInterrupts() e la riabilitazione alla fine interrupts()

  

* **descrivere funzionalità del piedino AREF/VIN/D0-1-2-...-N/GND/A0-1-2-...-N/RX/TX/SDA/SCL/... di Arduino/Wemos/...**

alimentazione:

- **VIN**: Ingresso di alimentazione per la board quando si utilizza un alimentatore esterno (7-12 V).

- **GND** (Ground): pin di massa.

- **PWD** (Pulse With Modulation): è possibile fornire una tensione variabile

- **3.3V/5V**: uscita di alimentazione per componenti esterni

- **AREF** (Analog REFerence): pin per fornire in input la tensione da usare come riferimento per l'analog input

- **IOREF** (Input/Output REFernce): fornisce il riferimento di tensione al quale la scheda Arduino opera. È usato per consentire agli shield di adattarsi alla tensione del microcontrollore (5V o 3.3V).

  

pin digitali:

- **DO - D13**: pin digitali che permettono di leggere/attuare oggetti booleana (acceso-spento)

- **PWM** (Pulse Width Modulation): solo su alcuni pin.

- **D0(RX)**: Ricezione dati seriali. Utilizzato per comunicazione seriale.

- **D1(TX)**: Trasmissione dati seriali. Utilizzato per comunicazione seriale.

  

pin analogici:

- **A0 - A5**: Possono leggere segnali analogici. Vengono utilizzati con il convertitore analogico-digitale (ADC) integrato per leggere tensioni variabili (di solito 0V a 5V) e convertirle in valori digitali (0 a 1023).

  

comunicazione:

- **SDA**: Per trasmettere dati tra dispositivi compatibili con il protocollo I2C.

- **SCL**: Fornisce il segnale di clock necessario per sincronizzare la trasmissione di dati I2C.

- **SPI** (Serial Peripheral Interface):

- **SS** (Slave Select): Per selezionare il dispositivo slave con cui comunicare.

- **MOSI** (Master Out Slave In): Per trasmettere dati al dispositivo slave.

- **MISO** (Master In Slave Out): Per ricevere dati dal dispositivo slave.

- **SCK** (Serial Clock): Fornisce il clock per la comunicazione SPI.

- **ICSP** (In-Circuit Serial Programming): Pin separati utilizzati per la programmazione del microcontrollore tramite un programmatore esterno. Comprende MOSI, MISO, SCK, RESET, VCC, e GND.

  

* **spiegare differenza fra GPIO digitale e analogico**

**digitali**: accettano 2 valori: 1 HIGH, 0 LOW

**analogici**: gestiscono diversi livelli di tensione (256 o 1024) tra 0V e 5V

  

## Rete: tutto, in dettaglio

  

* **spiegare livelli ISO/OSI e TCP/IP**

ISO/OSI:

- Livello fisico

- Livello di collegamento dati

- Livello di rete

- Livello di trasporto

- Livello di sessione

- Livello di presentazione

- Livello di applicazione

  

TCP/IP

- Livello di accesso alla rete

- Livello di rete

- Livello di trasporto

- Livello di applicazione

  

* **citare protocolli "normali" e "IoT", differenze, pro e contro**

- **MQTT** (Message Queuing Telemetry Transport): protocollo del tipo publisher/subscriver (observer/observee) basato su messaggi.

- I messaggi formati da *topic* (parole separate da "/") e *payload* (stringa UTF-8) sono inviati da un nodo *client* ad un *broker* al quale sono connessi.

- Il *broker* manda il messaggio a tutti i nodi che si sono iscritti a quel *topic*.

- I nodi che ricevono il messaggio eseguiranno una funzione callback definita da loro.

Funzioni da nodo connesso a broker

```

Subscribe(String subTopic, Function callback)

  

Publish(String topic, String message)

```

  

IoT

- **LoRa** (LOng RAnge): standard a livello fisico di rete wireless che definisce le modalità di trasmissione (modulazione) e le frequenze utilizzate.

- **LoRaWAN** (LOng RAnge Wild Area Network): standard che definisce lo strato MAC cioè il protocollo di trasmissione, indirizzamento, crittografia, formato dati, .. Lo standard mira a sostituire quello iFi per supportare la comunicazione tra sensori e gateway (che instradano verso nodi terminali o verso reti tradizionali) in contesti a basso consumo e lunghe portare.

vantaggi:

- comunicazioni bidirezionali

- buona robustezza alle interferenze

- consumi ridotti

- lungo raggio (anche Km)

- crittografia

- funzionamento indoor/outdoor

- bassi costi

  

nodi di 3 classi:

- Classe A: nodi bidirezionali che possono ricevere messaggi dopo aver inviato un messaggio

- Casse B: nodi bidirezionali come A in cui si possono anche definire finestre temporali di ricezione (necessitano sincronizzazione tra sorgente e ricevente)

- Classe C: nodi bidirezionali a ricezione continua (massimo consumo)

  

* **panoramica topologie di rete**

Nelle telecomunicazioni, l'evoluzione continua ha portato allo sviluppo di diverse tipologie di rete, distinguibili per:

- **Estensione Geografica**: superficie coperta (es. BAN11, PAN12, LAN13, MAN14, WAN15, GAN16)

- **Canale Trasmissivo**: mezzo utilizzato per la comunicazione

(es. Wireless, Cavo UTP, Linea Telefonica, Fibra Ottica,

Satellitari, Reti Elettriche)

- **Topologia**: modalità di connessione tra i i vari nodi (es. Lineare, Anello, Albero, Stella, Bus, Maglia)

  

Nei sistemi embedded, oltre alle classiche LAN, sono assai frequenti anche le BAN le PAN ed ovviamente in ambiente automobilistico le CAN.

In base allo scopo del dispositivo, può variare anche la topologia di collegamento:

- **Lineare** (daisy-chain): ogni nodo è collegato a due nodi adiacenti,tranne il primo e l’ultimo;

- **Anello** (ring): ogni nodo è collegato a due nodi adiacenti (i.e., formano un cerchio);

- **Albero** (tree): da ogni nodo possono partire catene lineari,

partendo dalla radice (root) muovendosi sulle foglie (leaf );

- **Stella** (star): tutti i nodi (spokes) sono collegati a un unico nodo centrale (hub);

- **Bus**: tutti i nodi sono collegati a un unico canale condiviso di comunicazione;

- **Maglia** (mesh): Tutti i nodi trasmettono dati ad altri (non tutti) nodi (grafo non necessariamente totalmente connesso).

  

Parlando di dispositivi IoT e di reti di sensori, le reti mesh

stanno riscontrando un notevole successo.

  

* **descrivere a grandi linee il protocollo OSC/MQTT**