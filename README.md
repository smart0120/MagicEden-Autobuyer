# Magic Eden Bot to Snipe the best offers
###### Created by Galiaf
------------
![Alt text](/screenshots/Screenshot_1.png?raw=true "Screenshot 1")
![Alt text](/screenshots/Screenshot_2.png?raw=true "Screenshot 2")
------------
- **[EN](https://github.com/Galiafer/MagicEden-Autobuyer#en)**
- **[RU](https://github.com/Galiafer/MagicEden-Autobuyer#ru)**
- **[TODO](https://github.com/Galiafer/MagicEden-Autobuyer#todo)**
------------

## EN
> This bot will help to buy NFT from the desired collection **at the lowest price**.

**ONLY WINDOWS for now, If the script at the beginning switches the window to MagicEden or only one window with Phantom Wallet is loaded, please restart the script**

**This bot does not guarantee you will buy NFT**, this bot simply goes faster than humans and automates everything since you do not have to click yourself.

### Tutorial
1. Clone the repository / Download zip file:

	`git clone https://github.com/Galiafer/MagicEden-Autobuyer.git`

	OR

	[Download Zip File](https://github.com/Galiafer/MagicEden-Autobuyer/archive/refs/heads/main.zip)

2. Be sure you have installed Python, [here is a link to download](https://www.python.org/downloads/)
3. Open **cmd** (command prompt)
4. Install **all python module**:

   `pip install -r requirements.txt`
5. Fill in all the data in `config.json`:
```json
{
"cooldown": 15 - minutes (How long will the bot wait for the next attempt),
"closeBrowser": true (Close browser after buying, false - No)
}
```
6. Fill in all the data in `.env` (But before rename .env-sample to .env):
```json
FILL EVERYTHING WITHOUT QUOTES

SEED_PHRASE=YOUR_SEED_PHRASE (Do Not Share This KEY)
PASSWORD=13372281111MEOW (Password from your Phantom Wallet)
```
7. Open **CMD** and go to directory:
 `cd /path/to/directory/`

8. Run the python file:

    windows : `python main.py`

------------
### Good luck to all.
------------

## RU
> Этот бот поможет купить НФТ из нужной коллекции **по самой низкой цене**.

**ПОКА ЧТО СКРИПТ РАБОТАЕТ ТОЛЬКО НА WINDOWS, если скрипт в начале переключает окно на MagicEden или загружается только одно окно с Phantom Wallet, пожалуйста, перезапустите скрипт**

**Этот бот не гарантирует вам 100% покупку НФТ**, он просто делает все быстрее, чем человек. Вы просто запускаете бота и ждете.

### Инструкция
1. Скопируйте репозиторий / Скачайте zip файл:

	`git clone https://github.com/Galiafer/MagicEden-Autobuyer.git`

	ИЛИ

	[Скачать Zip Файл](https://github.com/Galiafer/MagicEden-Autobuyer/archive/refs/heads/main.zip)

2. Удостоверьтесь, что у вас скачан Python, [ссылка на установку](https://www.python.org/downloads/)
3. Откройте **cmd** (командную строку)
4. Установите **все библиотеки**:

   `pip install -r requirements.txt`
5. Заполните все необходимые поля в файле `config.json`:
```json
{
"cooldown": 15 - минут (Как долго будет ждать бот перед следующей попыткой),
"closeBrowser": true (Закрыть браузер после покупки, false - Нет)
}
```
6. Заполните данные в `.env` (Но перед этим измените название файла с .env-sample на .env):
```json
ЗАПОЛНЯТЬ БЕЗ КАВЫЧЕК

SEED_PHRASE=ВАША_СИД_ФРАЗА (Никуда не публикуйте эту фразу)
PASSWORD=13372281111MEOW (Пароль от кошелька)
```
7. Откройте **CMD** (командную строку) и перейдите в директорию проекта:
 `cd /path/to/directory/`

8. Запустите файл:

    windows : `python main.py`

------------
### Хороших всем покупок.

## TODO:
1. Multisniping (Multi-collection sniping at the same time)
2. Multiaccounts
3. Snipe a certain amount of nft (Now you can only buy one nft)
4. Telegram Notification
