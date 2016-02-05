import MySQLdb

def openDatabase():
    #open database connection
    db=MySQLdb.connect("localhost","batsal","a","wn_pro_mysql")
    return db;


def getGlossory(word):
    db=openDatabase()
    cursor=db.cursor()
    
    sqlQuery="""SELECT 
                    w.word,
                    w.ss_type, 
                    g.gloss
                    
                FROM 
                    wn_synset w, 
                    wn_gloss g 
                WHERE 
                    w.synset_id=g.synset_id 
                        AND
                    w.word='%s'
                ORDER BY w.ss_type""" % word
    try:
        cursor.execute(sqlQuery)
        results=cursor.fetchall()
        wordMeanings=[]
        
        
        
        for row in results:
            wordMeaning=[]
            wordMeaning.append(row[0])
            wordMeaning.append ( row[1])
            wordMeaning.append ( row[2])
            wordMeanings.append(wordMeaning)
        db.close()
        
        return (wordMeanings);
    except:
        print "Error: unable to fetch data"
        db.close()
        return ;
    
    
    

'''wordMeanings=getGlossory('paper')
# Now print fetched result
print "%s :" % 'rock'

print " %s" % \
        (wordMeanings )
'''
      


'''
#for testing the  codes
db=openDatabase()
#prepare a cursor object using cursor() method
cursor=db.cursor()

#SQL query
sql= "SELECT w.word,g.gloss,w.ss_type from wn_synset w, wn_gloss g where w.synset_id=g.synset_id and w.word='test' "

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()

   print "%s :" % 'test'
   for row in results:
      word = row[0]
      gloss = row[1]
      wtype = row[2]
      # Now print fetched result
      print "(%s) %s" % \
             (wtype, gloss )
except:
   print "Error: unable to fecth data"
db=closeDatabase(db)
'''