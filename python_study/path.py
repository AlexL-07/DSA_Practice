from pathlib import Path

# Absolute Path
    # for windows: 
        # c:\Program Files\ Microsoft\etc\etc
    # for apple
        # /usr/local/bin
# Relative Path 

path = Path("ecommerce")
# this returns a path object leading to that specified package 
print(path.exists())
# this checks if that package exists or not 
# path.mkdir()
# makes a folder (in the main folder) named whatever you are passing into Path()
# path.rmdir()
    # removes the specific directory

path1 = Path()
    # '*.*' gives us all of the files inside the current directory returns an object that you can iterate over
for file in path1.glob('*'):
    print(file)