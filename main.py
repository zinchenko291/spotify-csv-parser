import argparse
import csv
import sys
from ytmusicapi import YTMusic as YTM

def createArgParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='Input csv file with songs', default='spotlistr-exported-playlist.csv')
    parser.add_argument('-o', '--output', type=str, help='Output file with urls on youtube music', default='urls.txt')
    return parser

class Song():
    artist    = ''
    trackName = ''
    albumName = ''

    def __init__(self, artist='', trackName='', albumName='') -> None:
        self.artist    = artist
        self.trackName = trackName
        self.albumName = albumName
    
    def print(self) -> None:
        print(f'Artist: {self.artist}\nTrack: {self.trackName}\nAlbum: {self.albumName}')

    def getArtist(self) -> str:
        return self.artist
    def getTrack(self) -> str:
        return self.trackName
    def getAlbum(self) -> str:
        return self.albumName

def parseCSV(file: str = 'spotlistr-exported-playlist.csv') -> list:
    songs = []
    with open(file, newline='') as csvfile:
        songsList = csv.reader(csvfile)
        for row in songsList:
            songs.append(Song(row[0], row[1], row[2]))
    return songs

def searchSongs(songs: list) -> list:
    YTMusic = YTM()
    urls = []
    urlBase = 'https://music.youtube.com/watch?v='
    for i in range(len(songs)):
        song = songs[i]
        searched = YTMusic.search(query=song.getArtist() + ' ' + song.getTrack(), filter='songs', limit=1)
        try:
            urls.append(urlBase + searched[0]['videoId'])
            
            # Log
            sys.stdout.write('\x1b[2K')
            print(f"Song {i + 1}/{len(songs)}: {searched[0]['artists'][0]['name']} - {searched[0]['title']}")
            print("\033[A\033[A")
        except IndexError:
            print('\n' + song.getArtist() + ' ' + song.getTrack() + ' - NOT FOUND')
    return urls

def writeUrlToFile(urls: list, file: str = 'urls.txt') -> None:
    with open(file, 'w') as f:
        w = ''
        for i in urls:
            w += i + '\n'
        f.write(w)


if __name__ == '__main__':
    parser = createArgParser()
    namespace = parser.parse_args(sys.argv[1:])
    writeUrlToFile(searchSongs(parseCSV(namespace.input)), namespace.output)