# IAEA Power Reactor Information System (PRIS) Dataset

This dataset contains data from the [IAEA PRIS](https://pris.iaea.org/pris/home.aspx) database. The information on each reactor in the database is presented on individual web pages in the following format: 

`https://pris.iaea.org/PRIS/CountryStatistics/ReactorDetails.aspx?current={num}` 

Where `{num}` should be replaced by a number in the range of 1 to 1084 (as of October 2022). There are several pages between pages 1 and 1084 that return an "Unauthorized Access" message. For example:

    - Using `{num}` = 98 corresponds to [Philippsburg-2](https://pris.iaea.org/PRIS/CountryStatistics/ReactorDetails.aspx?current=98) in Germany.
    - Using `{num}` = 99 yields an ["Unauthorized Access"](https://pris.iaea.org/PRIS/CountryStatistics/ReactorDetails.aspx?current=99) page. 

The "Unauthorized Access" page results have been filtered out of the dataset for a total of 685 entries. If an entry is missing a value for a given field, the value is set to "None".

## Column Definitions

 - **Country:** The country where the reactor is located.
 - **Energy Supplied:** Table of energy supplied over time.
 - **Name:** The name of the reactor. The unit number is denoted at the end of the name preceded by a dash (-).
 - **Reactor Type:** The type of the reactor.
 - **Model:** The model of the reactor.
 - **Status:** The operational status of the reactor.
 - **Design Net Capacity (MWe):** _
 - **Reference Unit Power (MWe):** _
 - **Gross Capacity (MWe):** _
 - **Thermal Capacity (MWt):** _
 - **Electricity Supplied (TWh):** The total energy supplied by the reactor as of 2021.
 - **Owner:** The owner of the reactor.
 - **Operator:** The operator of the reactor.
 - **Construction Start Date:** The date that construction of the reactor began.
 - **First Criticality Date:** The date that first criticality was achieved.
 - **First Grid Connection Date:** The date that the reactor was first connected to the electricity grid.
 - **Longterm Shutdown Date:** The date that the reactor entered longterm shutdown.
 - **Restart Date:** The date that the reactor was restarted.
 - **Permanent Shutdown Date:** The date that the reactor entered permanent shutdown.
 - **Commercial Operation Date:** The date that the reactor began commercial operation.
 - **Load Factor:** _
 - **Operation Factor:** _
 - **Energy Availability Factor:** _

## Notebooks

Jupyter notebooks that provide examples of working with the data.