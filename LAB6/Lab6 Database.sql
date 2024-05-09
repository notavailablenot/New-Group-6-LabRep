CREATE TABLE artists (
    ArtistId INT PRIMARY KEY,
    Name NVARCHAR(120) 
);

CREATE TABLE albums (
    AlbumId INT PRIMARY KEY,
    Title NVARCHAR(160) NULL,
    ArtistId INT,
    FOREIGN KEY (ArtistId) REFERENCES artists (ArtistId)
);

CREATE TABLE tracks (
    TrackId INT PRIMARY KEY,
    Name NVARCHAR(200) NULL,
    AlbumId INT,
    MediaTypeId INT,
    GenreId INT,
    Composer NVARCHAR(220) NULL,
    Milliseconds INT NULL,
    Bytes INT NULL,
    UnitPrice NUMERIC(18, 0) NULL,
    FOREIGN KEY (AlbumId) REFERENCES albums (AlbumId)
);
