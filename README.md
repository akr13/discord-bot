# discord-bot
A discord bot created for RU Hacks that helps students optimize their job hunting expeience.

## Inspiration
With an increase in the population of undergraduates pursuing computer science and engineering bachelor degrees, there has been a sudden surge in  the amount of applicants and competition for related roles. 
As a result, there is a demand for a system that minimizes the workload of reading each and every application.
Companies try to reduce the number of applications by running the documents through a filter to determine eligible applicants. 
Oftentimes, a candidate that is suitable for the role might be rejected without any human involvement.
Lumos was created to help such candidates!

## What it does
Lumos is a discord bot that helps users determine whether their résumés can be correctly parsed by software. The parser commands parses the user’s résumés and outputs it’s findings in .json and normal 
text format. 

## How we built it
Built using Discord.py.

## Challenges we ran into
Communication with a discord bot oftentimes consists of a command and a message, following a template like "!<command> <message>". Our biggest challenge was to figure out how to incorporate files into the communication stream. By sending and receiving files from the bot, we were able to create commands that parse and edit documents.

## Accomplishments that we're proud of
Our biggest accomplishment is shedding light on the life-cycle of an application for a specific role and providing tools to help a candidates get their application through the application tracking system and into the recruiter's hands!

## What's next for Lumos
Lumos can scale
