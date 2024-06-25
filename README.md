# DirSlideShow

## 概要

DirSlideShow は、Python で書かれた軽量なフォトスライドショーアプリケーションです。指定されたディレクトリ内の画像ファイルを自動的に検索し、ランダムな順序でスライドショーを表示します。

## 主な機能

- ディレクトリ内（サブディレクトリを含む）の画像ファイルを自動検索
- 画像をランダムにシャッフルして表示
- ループ時に新しくシャッフル
- exe ファイルへのドラッグ＆ドロップで簡単起動

## インストール

1. このリポジトリをクローンまたはダウンロードします。

2. 仮想環境を作成し、アクティベートします：

```bash
python -m venv venv
source venv/bin/activate  # Linuxの場合
venv\Scripts\activate  # Windowsの場合
```

3. 必要なパッケージをインストールします：

```bash
pip install pillow
```

## 使用方法

起動時にディレクトリを指定しない場合、DirSlideShow は、現在の作業ディレクトリ内の画像を検索します。

### Pythonスクリプトとして実行

```bash
python DirSlideShow.py [ディレクトリパス]
```

### exe ファイルとして実行

1. PyInstallerを使用してexeファイルを作成します：

```bash
pip install pyinstaller
pyinstaller --onefile slideshow.py
```

2. 生成された exe ファイルに画像フォルダをドラッグ＆ドロップするだけで、スライドショーが開始されます。

### 終了方法

- 以下のどちらかでスライドショーを修正します
  - `Esc` キーを押して終了します
  - ウィンドウ内で右クリックすると出てくるコンテキストメニューの「終了」を選択します

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルをご覧ください。

## 作者情報

rerofumi

## 変更履歴

- Jun.25.2024
    - first release
