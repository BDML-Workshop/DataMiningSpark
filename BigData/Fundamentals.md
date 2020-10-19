*Issued from "Le Cnam" course "[RCP216 : Ingénierie de la fouille et de la visualisation de données massives](http://cedric.cnam.fr/vertigo/Cours/RCP216)" By Michel Crucianu, Pierre Cubaud, Raphaël Fournier-S'niehotta, Marin Ferecatu, Nicolas Audebert and adapted for Cnam Liban by Pascal Fares*


# Text mining

The textual data contains potentially very useful information for the excavation. These data are present in very diverse forms, ranging from elaborate texts, with good grammatical conformity, to simple "word tags" (tags, often parts of words or words from a group lexicon), including incomplete sentences in SMS language, presenting a particular lexicon, numerous spelling errors and a very simplified syntax. This data is intended to be read and understood by humans, sometimes belonging to restricted groups.

If the data mining operations apply to a population of m observations, we consider here that each observation is characterized by a set of quantitative and nominal variables but also by a text (or list of keywords or tags). All of these texts will be denoted by T, with card (T) = m.

Beyond relatively superficial difficulties, such as lexical or syntactic nonconformity, the main problem in textual data mining is the "semantic gap", i.e. the gap between the interpretation that a computer can obtain. automatically from a text and the meaning of this same text for a human (of the category targeted by the text). Similar difficulties arise in mining other types of data, such as images or videos.

Even though textual data analysis methods are not yet able to bridge this semantic gap, it is nevertheless often possible to automatically extract useful information from textual data. The volume of data sometimes helps this process of extracting information. As textual data cannot be directly exploited by conventional data mining methods, prior processing is necessary depending on the objective.

## Objectives and applications