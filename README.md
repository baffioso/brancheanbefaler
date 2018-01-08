# Brancheanbefaler
[Notebook](https://github.com/baffioso/brancheanbefaler/blob/master/notebook/brancheanbefaler.ipynb) og webapp som ved hjælp af Machine Learning og data fra CVR kan anbefale brancher
![image](https://user-images.githubusercontent.com/7534153/34677306-fae58194-f48f-11e7-991f-d51621bc1212.png)

# Installation
* Gå ind i folderen brancheanbefaler og lav mapperne
mkdir app/model

* Udpak notebook/data.zip

* Lav virtualenv for henholdsvis notebook og app
```
virtualenv app/venv -p python3
virtualenv notebook/venv -p python3
```

* Aktiver virtuelt miljø og installer afhængigheder
```
source app/venv/bin/activate
pip3 install -r app/requirements.txt
deactivate

source notebook/venv/bin/activate
pip3 install -r notebook/requirements.txt
deactivate
```

* Åben notebook og kør koden gem modellen i .pkl format i under `app/model` ved at køre alle celler i notebook.
```
mkdir app/model
jupyter notebook
```

* Start app'en åben din browser på localhost:5000
```
cd app
source venv/bin/activate
python3 main.py
```

 * Åben din browser på `localhost:5000` og slå dig løs
