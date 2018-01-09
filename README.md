# Brancheanbefaler
[Notebook](https://github.com/baffioso/brancheanbefaler/blob/master/notebook/brancheanbefaler.ipynb) og webapp som ved hjælp af Machine Learning og data fra CVR kan anbefale brancher ud fra virksomhedsnavn.
![image](https://user-images.githubusercontent.com/7534153/34677306-fae58194-f48f-11e7-991f-d51621bc1212.png)

# Installation
* Udpak notebook/data.zip
* Gå ind i folderen brancheanbefaler
```bash
cd /sti/til/brancheanbefaler
```
* Lav virtualenv for henholdsvis notebook og app
```bash
virtualenv app/venv -p python3
virtualenv notebook/venv -p python3
```

* Aktiver virtuelt miljø og installer afhængigheder
```bash
source app/venv/bin/activate
pip3 install -r app/requirements.txt
deactivate

source notebook/venv/bin/activate
pip3 install -r notebook/requirements.txt
deactivate
```

* Opret mappe til modellen og kør alle celler notebooken. Herved gemmes modellen i .pkl format i under `app/model` som skal bruges i app'en.
```bash
mkdir app/model
jupyter notebook
```
<img src="https://user-images.githubusercontent.com/7534153/34687230-6278df22-f4ae-11e7-9a91-7248eb909490.png" width="250" />

* Start app'en
```bash
cd app
source venv/bin/activate
python3 main.py
```

 * Åben din browser på `localhost:5000` og slå dig løs
