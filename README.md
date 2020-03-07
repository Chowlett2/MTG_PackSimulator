# MTG_PackSimulator
A program that scrapes the web and creates samples of packs from a set in Magic: The Gathering
Magic the Gathering is a 30 year running competitive card game that prints hundreds to thousands
of new cards throughout each year.
Each new update is called an expansion and new cards can be purches in packs of 16 cards.
Each of these packs is different and it is essentially a gamble to see whether the contents therein
are valuable or not.
Using thousands of pack openings as well as some information provided by Wizards of the Coast (maker
of the game) I have made a simple algarithm that uses the statistical chances of pack contents and 
applies it to a dataframe that is scraped from a large Magic: The Gathering marketplace that buys and resells
these cards.

Packs generally consist of the following(in this order):
- 10 common cards with a 1/6 chance of the first card being a foil card of any rarity
- 3 uncommon cards
- A rare card with a 1/8 chance of a Mythic Rare card instead.
- A land card
- A token card

Each of these cards can vary drastically in market price.
In my program I have a function to generate samples of packs and average out the dollar value for each.
This was very useful to determine how much money one could expect to make or lose when purchasing packs
and later reselling the contents on the market.

Typically one can expect to lose close to a dollar per pack after reselling the contents.
