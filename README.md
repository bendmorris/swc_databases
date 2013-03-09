These files were used for teaching SQL databases at a Software Carpentry 
workshop.



SETUP contains installation instructions.


portal.sqlite is our SQLite database. It contains data from three sources:

main, species, plots:
S. K. Morgan Ernest, Thomas J. Valone, and James H. Brown. 2009. Long-term 
monitoring and experimental manipulation of a Chihuahuan Desert ecosystem near 
Portal, Arizona, USA. Ecology 90:1708.

mlh_species:
S. K. Morgan Ernest. 2003. Life history characteristics of placental non-volant mammals. Ecology 84:3402.

mom_species:
Felisa A. Smith, S. Kathleen Lyons, S. K. Morgan Ernest, Kate E. Jones, Dawn 
M. Kaufman, Tamar Dayan, Pablo A. Marquet, James H. Brown, and John P. Haskell. 
2003. Body mass of late Quaternary mammals. Ecology 84:3403.


SQL_COMMANDS.txt is a syntax reference. Since we'll be introducing a lot of
syntax quickly, use this reference to remember the clauses you've learned and
what order to put them in. Since we won't cover some topics in detail (INSERT,
CREATE TABLE, etc.), you can refer to these later.


sqlite.py is an example Python script to execute a query on a SQLite database,
loop over the results using a for loop, and print them to the screen.
sqlite2.py uses the matplotlib package to plot data from the database.


TASKS lists the tasks that we'll be completing during this course. We'll build
up to each of these by introducing the necessary concepts.