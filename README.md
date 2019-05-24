# Just Upload & Plot. Easy visualize tool via http.
UploadしてPlotするだけの簡単なhttp経由の可視化ツールです。

csvまたはxlsファイルをブラウザ上のUpload欄に上げるだけでさまざまな形式のグラフを描きます。

![gif](https://raw.githubusercontent.com/u1and0/uplot/pic/Peek%202019-05-22%2023-05.gif)


## csv, xlsを作成時の注意
* 1行目の1列目はx軸のタイトルになります。
* 1列目の2行目以降はx軸になります。
* 1行目の2列目以降は凡例になります。
* 2行目以降の2列目以降がデータになります。
* ファイル名はグラフタイトルになります。
* ファイル名に`_`が含まれている時、最初の`_`で区切られて、前半部分がグラフタイトル、後半部分がy軸のタイトルになります。


## 対応しているグラフ形式
* 'Line'
* 'Bar'
* 'Histogram'
* 'Pie'
* 'Polar'
* 'Box'
* 'Heatmap'
* '3D Scatter'
* '3D Surface'
* '2D Histogram'


## 対応予定のグラフ形式
* 'Contour'
* 'Candlestick'


# Install

## pip
あとでpypi登録予定

## Github
[GitHub u1and0/uplot](https://github.com/u1and0/uplot)
クローン後、`$ python uplot.py`


## Dockerhub
[Dockerhub u1and0/uplot](https://hub.docker.com/r/u1and0/uplot)


```sh
$ sudo docker pull u1and0/uplot
$ sudo docker run -d -p 8880:8880 u1and0/uplot
```

# USAGE
1. サーバーを立ち上げたらブラウザに`http//:localhost:8880`と打ち込みます。
2. csvかxlsで作成したファイルをドラッグ・アンド・ドロップしてグラフ種類を選択します。


# ScreenShots
![pic1](https://raw.githubusercontent.com/u1and0/uplot/pic/Screenshot%20from%202019-05-22%2022-54-04.png)
![pic2](https://raw.githubusercontent.com/u1and0/uplot/pic/Screenshot%20from%202019-05-22%2022-54-40.png)
![pic3](https://raw.githubusercontent.com/u1and0/uplot/pic/Screenshot%20from%202019-05-22%2022-55-05.png)
![pic4](https://raw.githubusercontent.com/u1and0/uplot/pic/Screenshot%20from%202019-05-22%2022-55-56.png)
![pic5](https://raw.githubusercontent.com/u1and0/uplot/pic/Screenshot%20from%202019-05-22%2022-56-11.png)
![pic6](https://raw.githubusercontent.com/u1and0/uplot/pic/Screenshot%20from%202019-05-22%2022-56-24.png)
![pic7](https://raw.githubusercontent.com/u1and0/uplot/pic/Screenshot%20from%202019-05-22%2022-56-41.png)
