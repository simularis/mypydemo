pyinstaller buildall.spec
pushd dist
7z a mypydemo.zip mypydemo
popd
