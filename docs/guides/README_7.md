# Forgotten Map Editor

**Development Status**: _Suspended_  
**Next release date**: _n/a_

**ForgottenMapEditor** is an otclient module, therefore it depends on OTClient. It is written using otclient's framework with modifications for reading and writing OT binary files and XML files.

## About this repository

This is the development repository.  We encourage you to find our buggy code, and please report in any bug you find. **Please label your issue report**!

## Authors

- Ahmed "[Fallen](https://github.com/decltype)" Samy <f.fallen45@gmail.com>  
- Eduardo "[edubart](https://github.com/edubart/)" Bart <edub4rt@gmail.com>

## Contributors / Thanks to

- [Sam](https://github.com/TheSumm) (Summ)  
- [Mateusz Pawlica](https://github.com/Crypton33) (Crypton33)  
- [Bruno Carvalho](https://github.com/comedinha) (BrunoDCC)  
- [Christian Johansson](https://github.com/dalkon) (Dalkon)

## Special thanks to

- [Chandler](http://otland.net/members/red.13708/) (Red)  
- [Mark Samman](https://github.com/marksamman)

## License

Licensed under MIT (Also known as "The Expat License"),  see LICENSE for more information.

## Contribute!

Contributions are always welcome.  You're welcome to contribute anything, whether documentation or code.  
If you're kind of lost on how to contribute, here is a short guide:

1. Make a GitHub account (if you don't have one) -
    GitHub have guidelines for newbies, so make sure to read them if you're lost.
2. Fork the repository
3. Commit your changes to YOUR repository.
4. Create a pull request (Click the pull request button on top of your fork) or
    notify me via e-mail <f.fallen45@gmail.com>

**Note**: You do not need to re-fork the project when a new change is made to this repository.  Use the following git commands:
 
```
git remote add https://github.com/decltype/forgottenmapeditor.git upstream
git fetch upstream
```  
Then whenever a new change is pushed into my repository, just use:   
```
git pull --rebase upstream master # pull from master branch
```  
Alternatively, you can use git pull with the repository URL everytime, but it's quicker to just add the remote. Like so:  
```
git pull --rebase https://github.com/decltype/forgottenmapeditor.git master
```

## Screenshots

Monday, September 02, 2013.  
![Screenshot](http://i.imgur.com/zcUeAyH.jpg)

Monday, July 29, 2013. (Town Dialog Preview)  
![Screenshot](http://i.imgur.com/b2lQ8Ft.jpg)

Saturday, Dec 7, 2013. (House Dialog Preview)  
![Screenshot](http://4.ii.gl/3551zW.png)

## See Also

[OTClient](https://github.com/edubart/otclient)

## Short guide for running

Warning: OTClient precompiled binaries may not be up-to-date (They're not updated frequently)!  
So some of the new features may not work at all.

You most likely would want to go for a compilation from scratch when you want to test/develop the master branch.  
After you have a working executable, place it on top of FME folder then run the executable.
