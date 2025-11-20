#### cos'è un S.O.?

Il sistema operativo è un elemento software atto a gestire le risorse hardware del sistema e offrire servizi agli altri software per interfacciarsi con appunto l'hardware a disposizione. 

Per quanto alcuni _microkernel_ (un microkernel è caratterizzato dal contenere la quantità minima possibile di codice che viene eseguito con accesso “supervisore”) abbiano trovato ampio mercato all'interno dei sistemi embedded, sono in genere utilizzati su CPU di piccole/medie dimensioni (es. le MCU) e per applicativi real-time. All'aumentare delle dimensioni e della complessità della CPU (come avviene nei SoC) _è di gran lunga preferibile utilizzare un kernel monolitico_(n kernel monolitico è caratterizzato della presenza all'interno del nucleo, oltre che dei driver e delle strutture di multiplexing dell’hardware, anche di una serie di servizi per la gestione dei processi e della comunicazione) (migliori tempi di sviluppo) e _libero_ (dovendo rispondere a forti necessità di personalizzazione e di contenimento dei costi)


Per questi motivi, per buona parte dei SoC di fascia alta presenti sul mercato, siano essi ARM o MIPS, Linux risulta essere il sistema operativo di riferimento.

#### cosa si intende con "preemptive multitasking"?

Preemptive Multitasking: attraverso un meccanismo basato su _interrupt_, viene sospeso il processo corrente, invocato lo _scheduler_ e sulla base di un diverso livello di priorità, viene eseguito un determinato processo. In questo modo _si cerca di garantire a tutti i processi un accesso pesato alle risorse hardware_, si differenzia dal non-preemptive dal fatto che ==aggiungere perché si differenzia== 

#### cos'è un filesystem?

==definire bene risposta con chat gpt== 

#### cos'è e a cosa serve un bootloader? che differenze ci sono tra un bootloader "classico" (da sistema operativo) e quello di un MCU?

Un bootloader è un software creato per consentire il caricamento del kernel, la selezione dei parametri di avvio e l’avvio vero e proprio del sistema

_In sistemi di elaborazione di complessità superiore alle MCU_, o comunque che eseguano sistemi operativi completi, la presenza di un _bootloader è da considerarsi necessaria_, è assai comune che ogni sistema operativo abbia un proprio bootloader

Un bootloader è a sua volta un piccolo “sistema operativo”, in quanto deve disporre degli elementi software necessari per poter accedere ai dispositivi di storage che contengono il sistema operativo. 

Nella maggioranza dei casi, nei PC si dispone di un _BIOS_ (ovvero di un firmware residente in una memoria FLASH/EEPROM della scheda madre) atto ad inizializzare l’hardware nel modo corretto, In sostanza _un bootloader_ per un computer tradizionale _trova parte del lavoro già svolto dal BIOS_

_Nei sistemi embedded_ la situazione è decisamente più complicata, in quanto, ad esclusione di casi eccezionali, il più delle volte _non dispongono di veri e propri BIOS_, bensì di assai più limitati e compatti _BootROM_.

Un BootROM esegue il numero minimo di operazioni per poter “_puntare_”(impostare il program counter della CPU su un indirizzo di memoria) verso una specifica area di storage, quella del bootloader, che deve farsi carico di tutte le operazioni necessarie per la prima configurazione dell’hardware al fine di poter caricare il sistema operativo.

questi dispositivi devono essere in grado di poter avviare il sistema utilizzando sorgenti assai diversificate tra di loro quali memorie NAND/NOR/FLASH, SDCard, USB, ethernet o addirittura delle connessioni lente quali serali UART ed SPI. 

La complessità di tale compito ha portato molti produttori a suddividere il bootloader in due componenti separati: 
- _pre-bootloader_: il primo si occupa delle inizializzazioni basilari quali la CPU, la RAM, i BUS ed un primo dispositivo di storage per “puntare” al bootloader completo
- _bootloader:_ offre anche una CLI, che può essere interattiva o meno, per poter selezionare il dispositivo e i parametri di boot

I bootloader, per evidenti restrizioni dal punto di vista della dimensione del codice, non possono essere flessibili come un kernel completo. 
Ciò comporta la _necessità di avere un bootloader specifico per ogni differente dispositivo_, ottimizzato e specializzato nella configurazione hardware presente.

__U-BOOT__

U-boot (nome completo “Das U-boot”, testualmente “Il bootloader universale”) è un progetto rilasciato con licenza libera GNU GPLv2. Solitamente classificato nella categoria “firmware”, è _uno dei bootloader più utilizzati nel mondo dei SoC_

==
