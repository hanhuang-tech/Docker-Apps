from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
	"https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492__340.jpg",
	"https://cdn.pixabay.com/photo/2015/04/23/21/59/tree-736877__340.jpg",
	"https://cdn.pixabay.com/photo/2015/11/16/14/43/cat-1045782__340.jpg",
	"https://cdn.pixabay.com/photo/2014/05/07/06/44/cat-339400__340.jpg",
	"https://cdn.pixabay.com/photo/2018/02/21/05/17/cat-3169476__340.jpg",
	"https://cdn.pixabay.com/photo/2017/12/11/15/34/lion-3012515__340.jpg",
	"https://cdn.pixabay.com/photo/2016/11/29/10/07/animal-1868911__340.jpg",
	"https://cdn.pixabay.com/photo/2017/01/12/21/42/amurtiger-1975790__340.jpg",
	"https://cdn.pixabay.com/photo/2014/11/03/17/40/leopard-515509__340.jpg",
	"https://cdn.pixabay.com/photo/2020/06/24/19/41/cat-5337501__340.jpg",
	"https://cdn.pixabay.com/photo/2020/10/27/07/40/cheetah-5689870__340.jpg",
	"https://cdn.pixabay.com/photo/2014/10/01/10/46/cat-468232__340.jpg",
	"https://cdn.pixabay.com/photo/2020/10/01/11/41/cat-5618328__340.jpg"
]

@app.route('/')
def index():
	url = random.choice(images)
	return render_template('index.html', url=url)

if __name__ == "__main__":
	app.run(host="0.0.0.0")
