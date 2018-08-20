import time
import requests
import requests_cache
import sqlite3
import os


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)


@app.route('/', methods=['GET', 'POST'])
def home():
	db = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '/us-census.db')
	c = db.cursor()
	#c.execute("DELETE FROM census_learn_sql WHERE age IS NULL;")
	c.execute("PRAGMA table_info(census_learn_sql)")
	data = c.fetchall() #all columns
	print("DB loaded")
	if request.method == 'POST':
		column = str(request.form.get('column')[1:])
		column = column.split("\n")[0]
		print(column)
		# user inputs

		query = 'SELECT ' + '"' +column+ '"' +  ' , ROUND(AVG(age),1), COUNT(*) FROM census_learn_sql GROUP BY ' + '"' +column+ '"' + ' ORDER by COUNT(*) DESC'
		c.execute(query)
		results = c.fetchall()
		#print('RESULTS : ' + column, results )

		# api call
		#url = "https://api.github.com/search/users?q=location:{0}+language:{1}".format(first, second)
		now = time.ctime(int(time.time()))
		#response = requests.get(url)
		#print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))
		# return json
		return jsonify(results)
	return render_template('index.html', columns = data)


if __name__ == '__main__':
    app.run(debug=True)
