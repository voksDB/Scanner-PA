Just as open data is not valuable unless it is detailed, opening data will not be effective if it necessarily involves risks to individual privacy - _più utilità o più privacy?_

PII - _"Personally identifiable information"_ 

“By data mining and other kinds of analytics, non-obvious and sometimes private information can be derived from data that, at the time of their collection, seemed to raise no, or only manageable, privacy issues” and that “one can never know what information may later be extracted from any particular collection of big data" 


“The versatility and power of re-identification algorithms imply that terms such as ‘personally identifiable’ and ‘quasi-identifier’ simply have no technical meaning. While some attributes may be uniquely identifying on their own, any attribute can be identifying in combination with others.”


### PRIVACY RISKS OF RELEASING DATA.

#### Re-identification

Re-identification occurs when _individual identities are inferred from data that has been de-identified_ (i.e., altered to remove individual identity from the data), and new information about those re-identified identities becomes known.

Re-identification involves the ability to learn information about individuals that would not otherwise be known. In many cases this new information can lead to a variety of harms for the re-identified individuals such as embarrassment, shame, identity theft, discrimination, and targeting for crime


#### False re-identification

When data is partially anonymous, individuals are at risk of _having sensitive facts incorrectly connected to them through flawed re-identification techniques_. This is especially likely to occur when open data is of low quality, and contains incorrect information or is difficult to interpret


Failed re-identification can be as troubling as successful re-identification. Individuals might have incorrect inferences made about them, which could lead to the same harms listed above for re-identification. These harms might be even more severe for false re-identification, since the outcomes will be based on false information or assumptions

#### Profile-building

Many companies and other groups compile information about individuals to build a digital profile of each person’s demographics, characteristics, habits, and preferences. Open data might contribute new information to these profiles.

Profiles built on data about individuals can be used to analyze and target information to specific segments of the population, thus facilitating algorithmic discrimination and exclusionary marketing.


#### Online discoverability  - (questa forse da verificare)

Information that is available online and accessible from an online search.
When information in open data appears in online search results, it appears to a wide audience who might not otherwise have sought out that information. 
any citizens will be concerned when open data associated with their identity can be discovered through online searches for their name or address. 

Multiple websites today post arrest records, including mug shots, to the Internet.27 While this information is public record, traditionally one would have needed to go to a courthouse to obtain it. Now one can find this information, even inadvertently, just by searching the name of someone who is listed by mug shot websites.

#### Direct identifiers - (principalmente trovare questi dati)

Features within a dataset that, on their own, identify individuals. These features (such as name, address, and Social Security Number) have traditionally been known as personally identifiable information (PII).

Because direct identifiers implicate an individual, all of the data tied to that identifier can be connected to the individual in question.

One dataset commonly released by open data programs is _property assessments_. Because this information includes each property’s owner and address (direct identifiers), most records can be connected to an individual. Any information attached to these records (such as property value, renovation history, and violations) can therefore also be traced back to an individual.


#### Quasi (a.k.a. indirect) identifiers

Features within a dataset that, in combination with other data, identify individuals. The ability to link features across datasets and learn about individuals is known as the mosaic effect.

Seemingly innocuous data can become revealing when combined with other datasets. Because quasi identifiers provide some information about individuals (although not enough by themselves to identify someone), they often facilitate linkage attacks (using the mosaic effect) that combine auxiliary information with quasi identifiers to identify individuals.


#### METADATA 

4 In a database of emails, for example, metadata contains the sender, recipient, and timestamp of emails. While email metadata does not contain the contents of emails, it can reveal patterns about how people correspond. As such, metadata often comprises behavioral records.

#### Addresses - cercare i documenti dove sono 

Street addresses or location names, Location data is often highly identifiable and can reveal particularly sensitive details about individuals. Because addresses identify where someone lives or where an event occurred, they are a rich source of information that make it easy to re-identify or learn intimate information about someone. Locations are also easy to link across datasets, facilitating the mosaic effect. 

Many cities publish data about 311 requests, which relate to topics such as street and sidewalk repairs, missed trash pickups, animal waste, and pest complaints. Because a typical entry in a 311 dataset includes the address for which the request is made along with a description of the issue, many requests can be re-identified to determine the requester and information about that person’s life.


#### coordinate geografiche 

Coordinates that identify a unique location on a map (i.e., latitude and longitude)

Geographic coordinates present the same vulnerabilities as addresses since they translate into locations. Because geographic coordinates do not by themselves reveal a location, however, they may appear to be less sensitive than the addresses they represent. This is misleading, as it is simple to obtain an address from geographic coordinates through a process known as “reverse geocoding

Crime data is one of the most heavily sought municipal datasets and, in the case of sexual assault-related incidents, one of the most sensitive. In order to protect the identities of victims when sharing open data, many jurisdictions remove the names and addresses associated with sexual assault incidents. However, such data occasionally includes the geographic coordinates of these incidents. Because it is relatively simple to obtain an address from geographic coordinates, this makes the victims of sexual assault highly identifiable. There are significant consequences if sexual assault victims are re-identified, including undue public scrutiny, violation of state shield laws, and potential chilling effects for future reports of sexual assault and domestic violence