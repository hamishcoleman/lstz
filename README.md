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

(Due to technical limitations with github markdown processing, the three
different shades of foreground colour and the current hour highlight with a
background colour are probably not visible to you in this example)

<pre>
$ ./lstz.py

off name      tzna time    hours                                                                   
+13 Auckland  NZDT 05:44+1 21 22 23     1  2  3  4[ 5] 6  7  8 <b> 9</b> <b>10</b> <b>11</b> <b>12</b> <b>13</b> <b>14</b> <b>15</b> <b>16</b> 17 18 19 20 
+11 Melbourne AEDT 03:44+1 19 20 21 22 23     1  2[ 3] 4  5  6  7  8 <b> 9</b> <b>10</b> <b>11</b> <b>12</b> <b>13</b> <b>14</b> <b>15</b> <b>16</b> 17 18 
 +9 Kyoto     JST  01:44+1 17 18 19 20 21 22 23   [ 1] 2  3  4  5  6  7  8 <b> 9</b> <b>10</b> <b>11</b> <b>12</b> <b>13</b> <b>14</b> <b>15</b> <b>16</b> 
 +8 HongKong  HKT  00:44+1 <b>16</b> 17 18 19 20 21 22 23[  ] 1  2  3  4  5  6  7  8 <b> 9</b> <b>10</b> <b>11</b> <b>12</b> <b>13</b> <b>14</b> <b>15</b> 
 +2 Helsinki  EET  18:44   <b>10</b> <b>11</b> <b>12</b> <b>13</b> <b>14</b> <b>15</b> <b>16</b> 17[18]19 20 21 22 23     1  3  3  4  5  6  7  8 <b> 9</b> 
 +1 Madrid    CET  17:44   <b> 9</b> <b>10</b> <b>11</b> <b>12</b> <b>13</b> <b>14</b> <b>15</b> <b>16</b>[17]18 19 20 21 22 23     2  2  3  4  5  6  7  8 
  ⌂ London    GMT  16:44    8 <b> 9</b> <b>10</b> <b>11</b> <b>12</b> <b>13</b> <b>14</b> <b>15</b><b>[16]</b>17 18 19 20 21 22 23  1  1  2  3  4  5  6  7 
  ⌂ UTC       UTC  16:44    8 <b> 9</b> <b>10</b> <b>11</b> <b>12</b> <b>13</b> <b>14</b> <b>15</b><b>[16]</b>17 18 19 20 21 22 23     1  2  3  4  5  6  7 
 -5 Chicago   CDT  11:44    3  4  5  6  7  8 <b> 9</b> <b>10</b><b>[11]</b><b>12</b> <b>13</b> <b>14</b> <b>15</b> <b>16</b> 17 18 19 20 21 22 23     1  2 
 -7 Pacific   PDT  09:44    1  2  3  4  5  6  7  8<b>[ 9]</b><b>10</b> <b>11</b> <b>12</b> <b>13</b> <b>14</b> <b>15</b> <b>16</b> 17 18 19 20 21 22 23    
</pre>
