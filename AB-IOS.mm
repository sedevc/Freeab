<map version="freeplane 1.3.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="AUTOBURNER CPU" ID="ID_1723255651" CREATED="1283093380553" MODIFIED="1409653085561"><hook NAME="MapStyle" zoom="2.09">

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node">
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right">
<stylenode LOCALIZED_TEXT="default" MAX_WIDTH="600" COLOR="#000000" STYLE="as_parent">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.note"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="10"/>
<node TEXT="OUTPUT" POSITION="right" ID="ID_112193941" CREATED="1409490411870" MODIFIED="1409490431893">
<edge COLOR="#ff00ff"/>
<node TEXT="GPIO17" ID="ID_113419805" CREATED="1409490411870" MODIFIED="1409492738954">
<node TEXT="SCREW MOTOR RELAY" ID="ID_1834449860" CREATED="1409490411870" MODIFIED="1409492757146"/>
</node>
<node TEXT="GPIO18" ID="ID_1542167010" CREATED="1409490411870" MODIFIED="1409492926689">
<node TEXT="FAN MOTOR PWM" ID="ID_1089459203" CREATED="1409490411870" MODIFIED="1409492769050"/>
</node>
<node TEXT="GPIO21" ID="ID_601145721" CREATED="1409490411870" MODIFIED="1409492780187">
<node TEXT="ELECTRIC LIGHTER RELAY" ID="ID_1594640739" CREATED="1409490411870" MODIFIED="1409492801132"/>
</node>
<node TEXT="GPIO22" ID="ID_835181102" CREATED="1409490411870" MODIFIED="1409492813180">
<node TEXT="BOILER ON/OFF RELAY" ID="ID_1309487801" CREATED="1409490411870" MODIFIED="1409492828509"/>
</node>
<node TEXT="GPIO22" ID="ID_852179797" CREATED="1409490411870" MODIFIED="1409492813180">
<node TEXT="RESERV" ID="ID_389529134" CREATED="1409490411870" MODIFIED="1409946217853"/>
</node>
<node TEXT="GPIO22" ID="ID_861653215" CREATED="1409490411870" MODIFIED="1409492813180">
<node TEXT="RESERV" ID="ID_1000710247" CREATED="1409490411870" MODIFIED="1409946223113"/>
</node>
</node>
<node TEXT="INPUT" POSITION="left" ID="ID_585682165" CREATED="1409490489761" MODIFIED="1409653056584">
<edge COLOR="#00ffff"/>
<node TEXT="GPIO07" ID="ID_758424509" CREATED="1409490489761" MODIFIED="1409652574801">
<hook NAME="FirstGroupNode"/>
</node>
<node TEXT="GPIO09" ID="ID_457895591" CREATED="1409490489761" MODIFIED="1409652556861"/>
<node TEXT="GPIO10" ID="ID_694684442" CREATED="1409490489761" MODIFIED="1409652565597"/>
<node TEXT="GPIO11" ID="ID_1700133507" CREATED="1409490489761" MODIFIED="1409652570317"/>
<node TEXT="SPI MAX6675" ID="ID_1010253686" CREATED="1409652574797" MODIFIED="1409652599342">
<hook NAME="SummaryNode"/>
<node TEXT="FIRE TEMP EGT K-TYPE" ID="ID_545999616" CREATED="1409490489761" MODIFIED="1409660445404"/>
</node>
<node TEXT="GPIO08" ID="ID_1027061637" CREATED="1409490489761" MODIFIED="1409492030518">
<hook NAME="FirstGroupNode"/>
</node>
<node TEXT="GPIO09" ID="ID_1023118862" CREATED="1409490489761" MODIFIED="1409490612492"/>
<node TEXT="GPIO10" ID="ID_107807125" CREATED="1409490489761" MODIFIED="1409490624348"/>
<node TEXT="GPIO11" ID="ID_1074188992" CREATED="1409490614720" MODIFIED="1409490631629"/>
<node TEXT="SPI ADC CONVERTER" ID="ID_1982591530" CREATED="1409492030505" MODIFIED="1409492228967">
<hook NAME="SummaryNode"/>
<node TEXT="CH00" ID="ID_573146483" CREATED="1409492071005" MODIFIED="1409492185221">
<node TEXT="LAMBDA 0-5V" ID="ID_167692868" CREATED="1409492071005" MODIFIED="1409493320895"/>
</node>
<node TEXT="CH01" ID="ID_200363974" CREATED="1409492071005" MODIFIED="1409492188821">
<node TEXT="ANALOG 0-5V" ID="ID_619708807" CREATED="1409492071005" MODIFIED="1409653207779"/>
</node>
<node TEXT="CH02" ID="ID_369884701" CREATED="1409492071005" MODIFIED="1409492191638">
<node TEXT="24V RELAY IN" ID="ID_755706526" CREATED="1409492071005" MODIFIED="1409493396946"/>
</node>
<node TEXT="CH03" ID="ID_1948424932" CREATED="1409492071005" MODIFIED="1409492194742">
<node TEXT="24V RELAY IN" ID="ID_1931971163" CREATED="1409492071005" MODIFIED="1409493396946"/>
</node>
<node TEXT="CH04" ID="ID_444250312" CREATED="1409492071005" MODIFIED="1409492198662">
<node TEXT="24V RELAY IN" ID="ID_991185737" CREATED="1409492071005" MODIFIED="1409493396946"/>
</node>
<node TEXT="CH05" ID="ID_444503244" CREATED="1409492071005" MODIFIED="1409492201400">
<node TEXT="24V RELAY IN" ID="ID_1919802766" CREATED="1409492071005" MODIFIED="1409493396946"/>
</node>
<node TEXT="CH06" ID="ID_149360131" CREATED="1409492071005" MODIFIED="1409492204455">
<node TEXT="24V RELAY IN" ID="ID_1434362562" CREATED="1409492071005" MODIFIED="1409493396946"/>
</node>
<node TEXT="CH07" ID="ID_1304109158" CREATED="1409492178724" MODIFIED="1409492209607">
<node TEXT="24V RELAY IN" ID="ID_1783404793" CREATED="1409492071005" MODIFIED="1409493396946"/>
</node>
</node>
<node TEXT="GPIO23" ID="ID_1752525499" CREATED="1409490489761" MODIFIED="1409493127943">
<node TEXT="SW AUTO/MAN" ID="ID_95207483" CREATED="1409490489761" MODIFIED="1409493164378"/>
</node>
<node TEXT="GPIO24" ID="ID_952105082" CREATED="1409490489761" MODIFIED="1409493138920">
<node TEXT="SW MAN SCREW" ID="ID_1499865013" CREATED="1409490489761" MODIFIED="1409493175226"/>
</node>
<node TEXT="GPIO25" ID="ID_844093558" CREATED="1409490489761" MODIFIED="1409493145736">
<node TEXT="SW MAN FAN" ID="ID_798983788" CREATED="1409490489761" MODIFIED="1409493185737"/>
</node>
<node TEXT="GPIO04" ID="ID_632288886" CREATED="1409652653749" MODIFIED="1409653056583" VSHIFT="35">
<node TEXT="DS18B20" ID="ID_1726265153" CREATED="1409652653749" MODIFIED="1409652695218">
<node TEXT="TEMP BOILER" ID="ID_236215980" CREATED="1409652653749" MODIFIED="1409652724082"/>
</node>
<node TEXT="DS18B20" ID="ID_1267283794" CREATED="1409652653749" MODIFIED="1409652712962">
<node TEXT="TEMP FIRE" ID="ID_870961801" CREATED="1409652653749" MODIFIED="1409652734370"/>
</node>
<node TEXT="DS18B20" ID="ID_1427938082" CREATED="1409652653749" MODIFIED="1409652712962">
<node TEXT="TEMP BYPASV.IN" ID="ID_1626889025" CREATED="1409652653749" MODIFIED="1409660370690"/>
</node>
<node TEXT="DS18B20" ID="ID_1991520249" CREATED="1409652653749" MODIFIED="1409652712962">
<node TEXT="TEMP BYPASV.OUT" ID="ID_124879343" CREATED="1409652653749" MODIFIED="1409660402458"/>
</node>
</node>
</node>
<node TEXT="USB" POSITION="right" ID="ID_372379462" CREATED="1409652892169" MODIFIED="1409653012798" HGAP="29" VSHIFT="26">
<edge COLOR="#00007c"/>
<node TEXT="USB1" ID="ID_1644695456" CREATED="1409652892169" MODIFIED="1409652901284">
<node TEXT="WLAN" ID="ID_712011637" CREATED="1409652892169" MODIFIED="1409652937947"/>
</node>
<node TEXT="USB2" ID="ID_554709216" CREATED="1409652892169" MODIFIED="1409652917977"/>
<node TEXT="USB3" ID="ID_1658181419" CREATED="1409652892169" MODIFIED="1409652921353"/>
<node TEXT="USB4" ID="ID_1353022983" CREATED="1409652892169" MODIFIED="1409652925545"/>
</node>
<node TEXT="ETHERNET" POSITION="left" ID="ID_855209859" CREATED="1409652949372" MODIFIED="1409652963130" HGAP="-191" VSHIFT="-6">
<edge COLOR="#007c00"/>
</node>
<node TEXT="POWER +5V" POSITION="right" ID="ID_368165296" CREATED="1409652989035" MODIFIED="1409653085560" HGAP="34" VSHIFT="14">
<edge COLOR="#7c007c"/>
</node>
</node>
</map>
