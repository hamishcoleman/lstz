Sometimes it is useful to just show a list of the time in different timezones.

## Configure

Create a file in `~/.config/lstz/tz.yml` containing the configuration.

E.G:

```
home: Australia/Melbourne

zones:
    Australia/Melbourne: Melbourne
    Hongkong: HongKong
    Europe/London: London
```

## Example Output

<pre>
$ ./lstz.py

off name      tzna time    hours                                                                   
+13 Auckland  NZDT 05:44+1 21 22 23     1  2  3  4 <span style="color:white;background-color:black;"> 5</span>  6  7  8 <span style="font-weight:bold;"> 9</span> <span style="font-weight:bold;">10</span> <span style="font-weight:bold;">11</span> <span style="font-weight:bold;">12</span> <span style="font-weight:bold;">13</span> <span style="font-weight:bold;">14</span> <span style="font-weight:bold;">15</span> <span style="font-weight:bold;">16</span> 17 18 19 20 
+11 Melbourne AEDT 03:44+1 19 20 21 22 23     1  2 <span style="color:white;background-color:black;"> 3</span>  4  5  6  7  8 <span style="font-weight:bold;"> 9</span> <span style="font-weight:bold;">10</span> <span style="font-weight:bold;">11</span> <span style="font-weight:bold;">12</span> <span style="font-weight:bold;">13</span> <span style="font-weight:bold;">14</span> <span style="font-weight:bold;">15</span> <span style="font-weight:bold;">16</span> 17 18 
 +9 Kyoto     JST  01:44+1 17 18 19 20 21 22 23    <span style="color:white;background-color:black;"> 1</span>  2  3  4  5  6  7  8 <span style="font-weight:bold;"> 9</span> <span style="font-weight:bold;">10</span> <span style="font-weight:bold;">11</span> <span style="font-weight:bold;">12</span> <span style="font-weight:bold;">13</span> <span style="font-weight:bold;">14</span> <span style="font-weight:bold;">15</span> <span style="font-weight:bold;">16</span> 
 +8 HongKong  HKT  00:44+1 <span style="font-weight:bold;">16</span> 17 18 19 20 21 22 23 <span style="color:white;background-color:black;">  </span>  1  2  3  4  5  6  7  8 <span style="font-weight:bold;"> 9</span> <span style="font-weight:bold;">10</span> <span style="font-weight:bold;">11</span> <span style="font-weight:bold;">12</span> <span style="font-weight:bold;">13</span> <span style="font-weight:bold;">14</span> <span style="font-weight:bold;">15</span> 
 +2 Helsinki  EET  18:44   <span style="font-weight:bold;">10</span> <span style="font-weight:bold;">11</span> <span style="font-weight:bold;">12</span> <span style="font-weight:bold;">13</span> <span style="font-weight:bold;">14</span> <span style="font-weight:bold;">15</span> <span style="font-weight:bold;">16</span> 17 <span style="color:white;background-color:black;">18</span> 19 20 21 22 23     1  3  3  4  5  6  7  8 <span style="font-weight:bold;"> 9</span> 
 +1 Madrid    CET  17:44   <span style="font-weight:bold;"> 9</span> <span style="font-weight:bold;">10</span> <span style="font-weight:bold;">11</span> <span style="font-weight:bold;">12</span> <span style="font-weight:bold;">13</span> <span style="font-weight:bold;">14</span> <span style="font-weight:bold;">15</span> <span style="font-weight:bold;">16</span> <span style="color:white;background-color:black;">17</span> 18 19 20 21 22 23     2  2  3  4  5  6  7  8 
  ⌂ London    GMT  16:44    8 <span style="font-weight:bold;"> 9</span> <span style="font-weight:bold;">10</span> <span style="font-weight:bold;">11</span> <span style="font-weight:bold;">12</span> <span style="font-weight:bold;">13</span> <span style="font-weight:bold;">14</span> <span style="font-weight:bold;">15</span> <span style="font-weight:bold;"></span><span style="font-weight:bold;color:white;background-color:black;">16</span> 17 18 19 20 21 22 23  1  1  2  3  4  5  6  7 
  ⌂ UTC       UTC  16:44    8 <span style="font-weight:bold;"> 9</span> <span style="font-weight:bold;">10</span> <span style="font-weight:bold;">11</span> <span style="font-weight:bold;">12</span> <span style="font-weight:bold;">13</span> <span style="font-weight:bold;">14</span> <span style="font-weight:bold;">15</span> <span style="font-weight:bold;"></span><span style="font-weight:bold;color:white;background-color:black;">16</span> 17 18 19 20 21 22 23     1  2  3  4  5  6  7 
 -5 Chicago   CDT  11:44    3  4  5  6  7  8 <span style="font-weight:bold;"> 9</span> <span style="font-weight:bold;">10</span> <span style="font-weight:bold;"></span><span style="font-weight:bold;color:white;background-color:black;">11</span> <span style="font-weight:bold;">12</span> <span style="font-weight:bold;">13</span> <span style="font-weight:bold;">14</span> <span style="font-weight:bold;">15</span> <span style="font-weight:bold;">16</span> 17 18 19 20 21 22 23     1  2 
 -7 Pacific   PDT  09:44    1  2  3  4  5  6  7  8 <span style="font-weight:bold;"></span><span style="font-weight:bold;color:white;background-color:black;"> 9</span> <span style="font-weight:bold;">10</span> <span style="font-weight:bold;">11</span> <span style="font-weight:bold;">12</span> <span style="font-weight:bold;">13</span> <span style="font-weight:bold;">14</span> <span style="font-weight:bold;">15</span> <span style="font-weight:bold;">16</span> 17 18 19 20 21 22 23    
</pre>
