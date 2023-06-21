# make_musicdataset
playlist.wav, timeline -(split)-> audio segment * n  
playlist -(main)-> 30s audio segment * 

audio segment * n -(extract)-> csv (chroma_mean var, rms_mean var, spectral cetroid_mean var, spectral bandwidth_mean var)* n

split, main, extract: Requires code modification each time a file is loaded or saved
