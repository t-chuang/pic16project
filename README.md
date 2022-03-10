## Predicting Economic Status Based on Energy Production

### Name of group members

Tim Chuang

Heera Kamaraj

Jamie Lau

### Description

This project aims to use information regarding the type of energy production and amount to predict the economic status of a region in the US.

### Instructions for package requirements

Run ```conda create --name NEWENV --file requirements.txt```

### Description of demo file

The demo file is in the form of a Jupyter notebook. Individuals code cells can be run and markdown cells contain explanations of the code. The process of creating our model occurs step by step to take the data to form a decision tree.

Below is a preview of the data we will be working with.

![Data preview](/images/dataframe.png)

This is one example of a tree we have generated given max depth and other parameters.

![Tree](/images/tree.png)

In general, we find that our model has overfitting issues using the chosen predictor variables. Using sources of energy does not appear to be a good way of determining the economic status of a region. Results are shown in the visualization of our decision tree. Further potential extensions on our project is discussed under Scope and Limitations.

### Scope/limitations

We have taken only data of places where all 3 sources are generated. This is because for cases where no data is available, the data shows "0". This can be confused with places that DO have available data, but in actuality, have no sources of energy generated.

Some ideas would be to incorporate other columns of data into our prediction. The model we have generated seems to be relatively inaccurate which suggests that it may be difficult to predict economic factors based on source energy generation.

### License and terms of use

MIT license

### References and acknowledgement

https://www.rff.org/publications/data-tools/mapping-vulnerable-communities/
Paper by Daniel Raimi

https://doi.org/10.1038/s41560-020-0582-0

https://www.arc.gov/classifying-economic-distress-in-appalachian-counties/

https://www.aceee.org/sites/default/files/publications/researchreports/u1602.pdf

### Background and source of dataset

Dataset was provided by "Resources for the future" (RFF).

Note: For EPA EJScreen, data are aggregated from census block groups to the county level, with each block group weighted by population.
