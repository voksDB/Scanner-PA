Basata su un’architettura modulare con microservizi dockerizzati, TrasparenzAI è _riutilizzabile per progetti basati su tecniche di web scraping programmabile_. I componenti software sviluppati sono rilasciati alla comunità con licenza opensource

### Componenti principali

#### public site service

Public Sites Service mantiene nel proprio datastore locale le informazioni degli enti che possono essere inserite/aggiornate tramite gli OpenData di [IndicePA](https://trasparenzai.github.io/glossario.html#term-IndicePA), oppure inserite tramite appositi servizi endopoint REST.

L’idea è quella di avere una fonte facile da consultare e estendibile delle informazioni delle organizzazioni pubbliche da analizzare. 

di base questo servizio _non credo verrà riutilizzato nel mio progetto_

#### config service 

Config Service è il componente che si occupa di archiviare e distribuire alcune informazioni di configurazione dei servizi che compongono lo stack del progetto TrasparenzAI.

Config Service mantiene nel proprio datastore locale le configurazioni che sono fornite agli altri microservizi. Le configurazioni possono essere inserite/aggiornate tramite gli appositi endopoint REST presenti in questo servizio.

questo servizio _o non sarà utilizzato o verrà modificato_ 

#### result service 

Result Service fornisce alcuni servizi REST utilizzabili in produzione per:

> - inserire, aggiornare e cancellare all'interno del servizio le informazioni di una verifica effettuata su un sito web di una PA
>     
> - visualizzare i dati di una verifica su un sito web
>     
> - mostrare la lista delle verifiche effettuate
>     
> - esportare in CSV i risultati delle validazioni presenti

questo servizio _non verrà utilizzato_


#### result aggregator 

Result Aggregator Service fornisce alcuni servizi REST utilizzabili in produzione per:

> - inserire, aggiornare e cancellare all’interno del servizio le informazioni di una verifica effettuata su un sito web di una PA ed dei dati geografici degli enti pubblici
>     
> - esportare in geoJson i risultati delle validazioni presenti arricchiti con la geolicazzazione degli enti

#### Task scheduler service 

Task Scheduler Service è il componente che si occupa di avviare alcuni processi eseguiti a intervalli fissi

#### Rule service 

Rule Service è il componente che definisce ed implementa le regole relative al D.Lgs. n. 33-2013 sulla trasparenza nella PA.

Fornisce l’albero delle regole definito in [application.yaml](https://github.com/trasparenzai/rule-service/blob/main/src/main/resources/application.yaml#L66-L554) oppure all’interno del [Config Service](https://trasparenzai.github.io/components/config-service.html) , che quindi può essere modificato o ampliato sia attraverso variabili di ambiente o della JVM prima di avviare il servizio, oppure aggiornando la configurazione per poi successivamente invocare l’endpoint [dell’actuator](http://localhost:8080/actuator/refresh) per recepire le modifiche.

É possibile interagire con il servizio attraverso degli endpoint REST che permettono la consultazione dell’albero delle regole in formato **json**, e la verifica di una o più regole su un contenuto **html**

# Crawler service  

Il servizio ha il compito di interfacciarsi con i siti web visitati dalla piattaforma e recuperare le informazioni pubblicate via web. In particolare, riceve una richiesta di accesso al sito specificato dal Conductor e in risposta fornisce la pagina acquisita, codificandola in formato Base64, e interagisce con l’object store per l’archiviazione del contenuto della pagina e/o dello screenshot renderizzato dal browser.

In particolare, il webscraping-service si aspetta di _ricevere un JSON_ contenente i seguenti parametri:

- _url_: contiene l'url da visitare, anche privo di schema http/https

- _crawlingMode_: httpStream | htmlSource - contiene la modalità di crawling

- _saveObject_: False | True - indica se l'oggetto deve essere salvato nell'object store o semplicemente restituito in risposta alla richiesta

- _saveScreenshot_: False | True - indica se lo screenshot della pagina deve essere salvato nell'object store.


```json
{
    "url": "www.cnr.it",
    "crawlingMode": "htmlSource",
    "saveObject": True,
    "saveScreenshot": False,
}
```

Relativamente alle modalità di crawling, htmlSource prevede la renderizzazione della pagina mediante un browser pilotato dal Selenium-hub e l’estrazione dal browser del sorgente HTML.


==questo servizio potrebbe essere usato, ma potrebbe anche andare oltre lo scopo del progetto, di base il "crawling" viene chiesto in un'altra tesi"

di base penso che avrò già il file da analizzare, il software deve solo analizzare non recuperarlo. 

==nella parte 2 vedrò come integrarlo nel progetto" 

