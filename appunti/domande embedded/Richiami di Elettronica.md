#### Descrivere a grandi linee il funzionamento di un resistore/condensatore/transistor/etc./... citare utilizzi

- il _resistore_ è un componente elettronico che se applicato al circuito ne aumenta appunto
la resistenza, viene utilizzato per ridurre il flusso di corrente all'interno del circuito, molti sensori (foto-resistenze, potenziometri ) utilizzano la loro resistenza interna e variabile per esprimere un valore, Nelle applicazioni domestiche viene utilizzata ad esempio proprio al puro scopo di generare calore: la stufetta. 

per la loro caratteristica caduta di tensione, il “_partitore di tensione_”, una tensione di alimentazione può essere “divisa” (partizionata, appunto) in varie “sotto-tensioni”

___
`segue un piccolo focus sul condensatore, forse un overfocus`

- il _condensatore_ è un componente capace di accumulare (e scaricare) una carica elettrica. 
Idealmente è composto da due piastre metalliche (conduttive) ampie e ravvicinate

Questi elettroni rimangono asimmetricamente distribuiti anche quando si toglie alimentazione, Gli elettroni accumulati su una delle due piastre creano una differenza di potenziale che si può utilizzare applicando un carico ai capi del condensatore. 

Un condensatore _si può applicare a valle di un segnale sinusoidale_ per “_appiattirlo_”
La vera utilità “elettronica” del condensatore è nei circuiti RC (Resistenza-Condensatore)
permettono la “gestione” di segnali variabili nel tempo.

Vicino agli integrati si mettono piccoli condensatori (es. 100nF) per:
- assorbire disturbi
- stabilizzare la tensione locale,
- compensare richieste istantanee di corrente.

`come si carica e scarica il condensatore?`

Consideriamo un semplice circuito RC.  
La grandezza chiave è la **costante di tempo**:

$$\tau = RC$$
È il tempo necessario affinché il condensatore si carichi al **63,2%** della tensione finale o si scarichi al **36,8%** del valore iniziale.

si usa per le _temporizzazioni_, introduce un ritardo controllato
come _filtro_, smussa le variazioni rapide provenienti da esterno 


____


- il _transistor_ è il componente alla base dell'informatica, è un componente che esprime un valore a seconda della tensione che viene applicata al circuito. sono semiconduttori.

![[Pasted image 20251114175719.png]]
In elettronica digitale i transistor si usano in maniera “booleana” (on/off), cioè similmente a dei relè a stato solido
utilizzano un flusso di corrente (pur piccolo, ma non nullo) per pilotare la corrente di uscita, ma esiste anche una famiglia di transistor che utilizza una tecnologia che lavora “in tensione”, i cosiddetti FET (Field Effect Transistor)

==capire meglio i transistor e come si utilizzano in embedded==



altri componenti non citati nella domanda: 

- _diodo_ è un semiconduttore, I semiconduttori sono componenti fondamentali, I componenti “semiconduttori” prendono il nome dai cristalli che li contengono, tipicamente a base silicio, opportunamente “drogati”, si comportano, appunto, come semi-conduttori: conducono più o meno  corrente in funzione di varie condizioni al contorno, ad es. temperatura, luce, altre correnti “vicine”, eccetera.

il diodo ha la caratteristica di far passare la corrente in una sola direzione

- _interruttore_..... apre e chiude il circuito boh... 

- _il relay_ (o relè) è un interruttore elettromagnetico, l'apertura del circuito è comandata da un segnale elettrico che attiva un elettromagnete che spostando una lametta chiude il circuito. 

- _Pile, accumulatori, generatori, ..._, 
 ![[Pasted image 20251114164744.png]]



#### panoramica delle unità di misura (elettricità/elettronica) e loro significato

per far muovere gli elettroni in un circuito, serve una _tensione o potenziale elettrico_, che si misura in _volt_, è la forza che spinge gli elettroni nel circuito. 
mentre la quantità di corrente in un determinato periodo è l'_intensità_ e si misura in _ampere_

l'ampere corrisponde a _1 Coulomb/s_, il C, è corrisponde a 6 qualcosa alla 18 elettroni. 

la relazione tra tensione e intensità è espressa dalla legge di Ohm: 
$$I = \frac{V}{R}$$
dove R è la resistenza del circuito, che dipende dal materiale. 

la _potenza_ è il calore dissipato dal circuito
$$P = V*I - oppure - R * I^2   - oppure - V^2/R$$

#### spiegare i collegamenti serie e parallelo per resistori e condensatori

resistenze in serie si sommano le resistenze 
resistenze in parallelo $R = 1/R_1 + 1/R_2$
![[Pasted image 20251114165354.png]]
per i _condensatori_: 
Due (o più) condensatori in parallelo “sommano” i loro effetti, cioè la capacità totale del componente “aggregato”. 
![[Pasted image 20251114165618.png]]

#### descrivere leggi di Kirchhoff

la _legge di Kirchhoff delle correnti_ formalizza il fatto che in un “nodo” (punto di incontro di più percorsi all' interno di un circuito, giunzione)
le correnti entranti e le correnti uscenti si bilanciano, in parole povere “non si creano né spariscono elettroni”.
![[Pasted image 20251113174147.png]]

La _legge di Kirchhoff delle tensioni_  formalizza il fatto che in un circuito la somma algebrica delle tensioni è 0, in parole povere “non si creano né spariscono differenze di potenziale”

![[Pasted image 20251113174315.png]]

==si ma nell'effettivo cosa comportano queste leggi?==

___
#### differenza fra corrente alternata e continua

La differenza consta nel _comportamento degli elettroni_ che fluiscono nei conduttori, nel caso della corrente _continua_ essi si muovono sempre nella stessa direzione, nella _alternata_ cambiano verso, vanno cioè avanti e indietro secondo un periodo che prende il nome di “frequenza” che si misura in Hertz

altre differenze: 

nella _produzione_:
- la corrente _alternata_ viene prodotta _meccanicamente_, facendo ruotare un insieme di conduttori all'interno di un campo magnetico
- la corrente _continua_ invece viene prodotta _chimicamente_, e anche meccanicamente tramite dinamo

nell'_immagazzinamento: 
- corrente continua è immagazzinabile, negli “accumulatori” chimici o “condensatori” elettrostatici
- quella alternata non è direttamente accumulabile a meno di non trasformare l’energia elettrica associata in altri tipi di energia

per la corrente alternata è possibile trasformarla in continua attraverso un _trasformatore_, Nella sua forma base è composto da due bobine vicine, inducendo una corrente la cui tensione dipende da quella della prima bobina e dal rapporto fra i numeri di spire delle due bobine
![[Pasted image 20251113184945.png]]

`GTK:`
a distanza si deve trasportare tensione (forza) e corrente (intensità) dato che la potenza è il prodotto V × I. Purtroppo il calore dissipato da un conduttore è proporzionale al quadrato della intensità di corrente (R × I 2 ) ergo è più conveniente alzare la tensione per elevare l’energia trasportata

#### cos'è la potenza elettrica?

energia dissipata dal passaggio della corrente, guarda sopra.

#### cos'è un segnale?

um mezzo di trasmissione dell'informazione ? 
la corrente elettrica può essere un segnale no aspe la corrente forse è il mezzo , il segnale è una differenza della tensione? 

#### quale effetto ha un condensatore su un segnale variabile?

lo rende costante 

#### cosa si intende con "forma d'onda"?

In elettronica si parla spesso di “forme d’onda” per rappresentare segnali. 
Una forma d’onda è la rappresentazione cartesiana dell’andamento della grandezza elettrica (tensione o corrente). 

![[Pasted image 20251114152508.png]]
![[Pasted image 20251114152555.png]]

Regolari si esprime anche una “frequenza”, misurata in Hz (Hertz, cicli al secondo), un segnale sinusoidale a 50 Hz (la rete elettrica domestica) è quello il cui ciclo completo (da picco a picco) si svolge 50 volte al secondo.

L’abilità di leggere una forma d’onda ci permette di capire come funzionano i componenti elettrici/elettronici e anche di interpretare il funzionamento dei protocolli di comunicazione
#### spiegare V eff (efficace)

un _segnale sinusoidale_ (ma più in generale qualunque segnale variabile nel tempo) trasporta una “potenza” elettrica inferiore a quello ipotetico relativo all'ampiezza massima

la potenza cosiddetta “_efficace_” è una “integrazione” della potenza istantanea nel tempo.

per un segnale _perfettamente sinusoidale_, la “_tensione efficace_” si calcola
![[Pasted image 20251114153204.png]]


#### spiegare costante di tempo RC ( e circuiti RC già che ci siamo)

I cosiddetti “_Circuiti RC_” (Resistenza-Condensatore), nella loro forma più semplice sono composti da una sola resistenza e da un solo condensatore accoppiati in serie/parallelo, in due combinazioni:


![[Pasted image 20251114165748.png]]

mettiamo nel caso che in V in venga fornito un segnale con questa forma d'onda: 
![[Pasted image 20251114170019.png]]

- L’_integratore_, intuitivamente, funziona nel seguente modo:
il condensatore richiede del tempo per caricarsi, in particolare richiede un tempo _τ = R × C_ (chiamata costante di tempo del circuito RC) per arrivare al 63.2% della sua capacità, un altro τ per il successivo 63.2% del rimanente 36.8%. 
se il ciclo dell’onda quadra in ingresso è molto breve _il condensatore non fa mai in tempo a raggiungere la carica massima_ cioè l’ampiezza del segnale in uscita non arriva mai alla stessa ampiezza del segnale in ingresso;
![[Pasted image 20251114170433.png]]


- il  _differenziatore_, intuitivamente, funziona nel seguente modo:
durante la fase alta della quadra il condensatore si carica, ai capi della resistenza si forma un potenziale negativo che man mano che il condensatore si carica tende a 0, 
![[Pasted image 20251114170516.png]]
durante la fase 0 dell’onda quadra in ingresso; il condensatore si scarica sulla resistenza (invertendo il verso di scorrimento degli elettroni); generando una tensione positiva decrescente nel tempo ai capi di R; ecco il motivo della discesa relativamente dolce (figura 3.15) della tensione in uscita; se il ciclo dell’onda quadra in ingresso è molto lungo gli “impulsi” sono molto sottili e distanti tra loro; questa situazione peggiora al decrescere della frequenza.. 


#### descrivere leggi di Ohm e loro significato ???

boh $I=V*R$ i guess 
#### spiegare PWM e utilizzi

La PWM, Pulse Width Modulation, è un tipo di segnale che viene usato sia per _trasmettere informazione_ che per pilotare efficientemente _motori elettrici_  o altri oggetti immagino. 

Un segnale PWM semplice ha una forma d’onda “quadra”, tipicamente con un periodo fisso, ma non simmetrica, cioè la durata della semi-onda alta è raramente uguale alla durata della semi-onda bassa. 

La durata dell’impulso viene misurata in percentuale, si definisce _duty cycle_ e specifica la durata rispetto al periodo, ad esempio 50% definisce una PWM quadra simmetrica, 10% una quadra “accesa” per il 1/10 del periodo



Nel caso del pilotaggio dei carichi la PWM sfrutta la caratteristica _inerzia_ di alcuni carichi, per ottenere un effetto di per ottenere un effetto di “regolazione continua”. 

si può affermare che variando la durata dell’impulso varia la tensione efficace, e quindi la potenza che sto dando al motore. 

![[Pasted image 20251114174331.png]]


#### spiegare ponte "H"

Un circuito interessante per comandare un motore a corrente continua è il  “ponte H”, 
![[Pasted image 20251114183338.png]]

Chiudendo opportunamente (i.e., o S1, S4 o S2, S3 ovviamente mai S1, S2 o S3, S4 pena un
corto circuito sull'alimentazione) i contatti è facilissimo decidere il senso di rotazione del motore M a corrente continua. 

==credo di aver capito e non ci sia nulla da aggiungere ma nel caso controlla chat gpt== 

____
___

un oggetto basato su un materiale che cambia le sue proprietà elettriche al variare delle condizioni ambientali a cui è sottoposto (es foto resistenza con la luce )
#### panoramica generale su sensori "fisici", esempi

Sono sensori che producono un segnale **analogico**, cioè una grandezza _continua_ (tensione o corrente) proporzionale alla grandezza fisica misurata.

- termistori 
- fotoresistenze
- microfoni 
- potenziometro 
- tilt sensor, che chiude un contatto elettrico 

==di base guardare anche quelli a casa che hai==

#### panoramica generale su sensori "numerici", esempi

Sono sensori che includono **elettronica digitale interna**, spesso un ADC integrato, e **forniscono direttamente dati digitali** tramite un protocollo. 

tipo il rilevatore di umidità e temperatura. 

Sensori di distanza a ultrasuoni 
- Output digitale: impulsi che rappresentano il tempo di volo.

#### panoramica generale su attuatori, esempi

Un attuatore è un oggetto che cambia le sue proprietà meccaniche al variare dei segnali elettrici che gli vengono forniti. 

già citato il relè
Un semplice motore a corrente continua è un attuatore



==il capitolo è finito ma mancano da scrivere bene:==
#### panoramica generale su motori, esempi

ma tipo anello Pacinotti e compagnia?? io mi sparo quella roba ho capito 0 lol 

#### panoramica strumenti di misura, esempi, possibili problemi 

voltmetro, amperometro, multimetro??? 




