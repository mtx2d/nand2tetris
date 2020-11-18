```
(base) mqiu@DESKTOP-A88JPG4:~/workspace/nand2tetris/projects/10(master⚡) » rm /home/mqiu/workspace/nand2tetris/projects/10/syntax_analyzer/tests/TestTokenMain.xml &&  python3 syntax_analyzer/syntax_analyzer.py --source-path ./syntax_analyzer/tests/TestTokenMain.jack                                   255 ↵
(base) mqiu@DESKTOP-A88JPG4:~/workspace/nand2tetris/projects/10(master⚡) » sh ../../tools/TextComparer.sh syntax_analyzer/tests/TestTokenMain.xml Square/Main.xml 
```

Test SquareGame.jack
```
(base) mqiu@DESKTOP-A88JPG4:~/workspace/nand2tetris/projects/10(master○) » python3 syntax_analyzer/syntax_analyzer.py --source-path ./syntax_analyzer/tests/Square                            130 ↵
/home/mqiu/workspace/nand2tetris/projects/10/syntax_analyzer/tests/Square/SquareGame.xml already exists, skipping.
/home/mqiu/workspace/nand2tetris/projects/10/syntax_analyzer/tests/Square/Main.xml already exists, skipping.
/home/mqiu/workspace/nand2tetris/projects/10/syntax_analyzer/tests/Square/Square.xml already exists, skipping.
(base) mqiu@DESKTOP-A88JPG4:~/workspace/nand2tetris/projects/10(master○) » rm /home/mqiu/workspace/nand2tetris/projects/10/syntax_analyzer/tests/Square/SquareGame.xml
(base) mqiu@DESKTOP-A88JPG4:~/workspace/nand2tetris/projects/10(master⚡) » python3 syntax_analyzer/syntax_analyzer.py --source-path ./syntax_analyzer/tests/Square    
/home/mqiu/workspace/nand2tetris/projects/10/syntax_analyzer/tests/Square/Main.xml already exists, skipping.
/home/mqiu/workspace/nand2tetris/projects/10/syntax_analyzer/tests/Square/Square.xml already exists, skipping.
(base) mqiu@DESKTOP-A88JPG4:~/workspace/nand2tetris/projects/10(master⚡) » sh ../../tools/TextComparer.sh syntax_analyzer/tests/Square/SquareGame.xml Square/SquareGame.xml
Comparison ended successfully
```
