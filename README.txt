This is a project I worked on for the course "Programming for Cultural Heritage" at Pratt SILS in the fall of 2014.
I became interested in the Dreweatts Auction House because I am QA’ing the website for my job at the Frick Art Reference Library’s Web Archiving Initiative. 

As a student of art history/library science and as an archivist, I am passionate about the history of photography and will eventually be writing my art history master's thesis on the subject. I want to investigate the circumstances that have led to the establishment of photography as an "accepted high art form" and that conception's subsequent influence on the sales of photography at auction.  I am interested in seeing general trends, such aswhether works created during certain decades went for higher prices or how many works from a decade went unsold.

I selected 6 auctions that were photography based:
2011, May
2012, May
2012, November
2013, November
2014, February
2014, June

I scraped the URLS for each lot in the auction that was a photography based work. I gathered information about: artist; date the work was created; the price in GB Pounds for which the lot sold (or whether it was Unsold); the title of the work. This information wrote out to JSON files.  From there I used the date created to generate a decade in which the work was created. I continued to parse out the data.

The (year)_(month)_for_candlestick.py files use the data from the json files to perform several calculations: the total amount of money spent on each decade; the total number of works available for auction in a decade; the total number of works sold by decade; the highest price per decade; the lowest price per decade; the average price per decade; the median per decade.  

I still have one issue to solve.  I have not been able to get the median to calculate outside of the writerow.
