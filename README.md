# CSE363 HW1 README - Sniffer

This HW assignment more or less follows the spec given by the document.
A chunk of code is commented out - this is meant to capture credentials
from a POST request. Because it is outside the scope of the HW and would
"break the spec", it is commented out - but it is there if you'd like to take a look (Starting Line 19)

The default interface is to listen on all, but can of course be overridden by the -i flag.

The -r flag works as intended -that is, after opening, the program exits normally.

If -i and -r are given (or an expression), it should basically read the pcap and exit normally.

Multiple get requests loaded from a given website will output a series of HTTP prints.
This is simply because that's how get requests work.

Example output:

    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:52780 -> 151.139.128.10:80 www.neopets.com GET /
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:52780 -> 151.139.128.10:80 www.neopets.com GET /include/colorbox/base.css?v=1
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39798 -> 205.185.216.10:80 images.neopets.com GET /css/default.css?v=5
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39800 -> 205.185.216.10:80 images.neopets.com GET /css/themes/000_def_f65b1.css?v=10.22
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39802 -> 205.185.216.10:80 images.neopets.com GET /js/common.js?v=6
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /js/jquery-ui-1.8.17.min.js
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39804 -> 205.185.216.10:80 images.neopets.com GET /js/jquery-1.7.1.min.js
    Fri Feb 21 10:05:10 2020 TLS v1.2 192.168.1.100:51470 ->  172.217.10.138:443 safebrowsing.googleapis.com
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39808 -> 205.185.216.10:80 images.neopets.com GET /js/getbrowser.js?v=1
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39798 -> 205.185.216.10:80 images.neopets.com GET /n.js
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39800 -> 205.185.216.10:80 images.neopets.com GET /js/jquery.colorbox.min.js?v=1
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /transparent_spacer.gif
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39808 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/myaccount.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39804 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/customise.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39800 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/games.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39802 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/explore.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39798 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/news.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39808 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/community.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/shops.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39804 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/ncmall.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39802 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/premium.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39800 -> 205.185.216.10:80 images.neopets.com GET /template/signup/signup-banner.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /np-facebook.jpg
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39798 -> 205.185.216.10:80 images.neopets.com GET /homepage/marquee/tonu_day_2011.jpg
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39804 -> 205.185.216.10:80 images.neopets.com GET /homepage/marquee/wintermysterycaps.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39808 -> 205.185.216.10:80 images.neopets.com GET /homepage/marquee/game_pakiko.jpg
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39802 -> 205.185.216.10:80 images.neopets.com GET /homepage/marquee/random_contest_bb.jpg
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39800 -> 205.185.216.10:80 images.neopets.com GET /homepage/promo/2020/mall/2020_wintershop.jpg
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /homepage/neopoint_icon.gif
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39798 -> 205.185.216.10:80 images.neopets.com GET /homepage/neocash_icon.gif
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39800 -> 205.185.216.10:80 images.neopets.com GET /items/bg_advc2019_christmaswindow.gif
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39808 -> 205.185.216.10:80 images.neopets.com GET /items/mall_bg_sunsetpetpetgarden.gif
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /items/clo_hol_themed_earrings.gif
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39798 -> 205.185.216.10:80 images.neopets.com GET /items/mall_fg_surroundbypresents.gif
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39804 -> 205.185.216.10:80 images.neopets.com GET /homepage/spotlights/6_sosuleaf_20190924.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:52780 -> 151.139.128.10:80 www.neopets.com GET /sbbi/?sbbpg=utMedia&vii=5h24e4a2a53c8358034c95a4fb346226c6e5cc16e1a5c076c207532864fdaaa0zbzcl7g5
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39800 -> 205.185.216.10:80 images.neopets.com GET /homepage/spotlights/22_nicobutts_20180130.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:57038 -> 205.185.216.42:80 dynimages.neopets.com GET /nh/spotlight/entry/meredith177644/1.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39798 -> 205.185.216.10:80 images.neopets.com GET /homepage/spotlights/2_mermaid_in_space_20190221.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39808 -> 205.185.216.10:80 images.neopets.com GET /homepage/spotlights/1_rainbowdragon3200_20190211.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /games/clicktoplay/tm_1377.gif
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39802 -> 205.185.216.10:80 images.neopets.com GET /games/clicktoplay/tm_1367.gif
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39804 -> 205.185.216.10:80 images.neopets.com GET /games/clicktoplay/tm_1370.gif
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39800 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/rotations/13.png
    Fri Feb 21 10:05:10 2020 HTTP 192.168.1.100:39798 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/privacypolicy.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39808 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/divider.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/safetytips.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39802 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/contactus.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39804 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/aboutus.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39800 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/referral.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/help.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39808 -> 205.185.216.10:80 images.neopets.com GET /help/bumper/headers/leaving-neopia.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39798 -> 205.185.216.10:80 images.neopets.com GET /help/bumper/headers/log-in-to-facebook.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39802 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/navigation/follow-us-on.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39804 -> 205.185.216.10:80 images.neopets.com GET /facebook-icon.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /template/popups/login/login-to-neopets.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39804 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/header_bg.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39802 -> 205.185.216.10:80 images.neopets.com GET /themes/000_def_f65b1/footer_bg.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39800 -> 205.185.216.10:80 images.neopets.com GET /dark-semi-trans.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39808 -> 205.185.216.10:80 images.neopets.com GET /help/bumper/bg.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39798 -> 205.185.216.10:80 images.neopets.com GET /help/bumper/buttons/yes.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:39806 -> 205.185.216.10:80 images.neopets.com GET /help/bumper/buttons/no.png
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:52780 -> 151.139.128.10:80 www.neopets.com GET /sbbi/?sbbpg=sbbShell&gprid=nO&sbbgs=h4425c383c54b42665c6150627384da0bc75&ddl=3
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:57038 -> 205.185.216.42:80 dynimages.neopets.com GET /nh/spotlight/entry/meredith177644/1.png?lm=1430609127
    Fri Feb 21 10:05:11 2020 HTTP 192.168.1.100:52780 -> 151.139.128.10:80 www.neopets.com GET /favicon.ico
    Fri Feb 21 10:05:11 2020 TLS v1.2 192.168.1.100:45892 ->  130.211.16.53:443 d.joinhoney.com
    Fri Feb 21 10:05:12 2020 HTTP 192.168.1.100:52780 -> 151.139.128.10:80 www.neopets.com POST /sbbi/?sbbpg=sbbShell&gprid=nO&sbbgs=h4425c383c54b42665c6150627384da0bc75&ddl=3
    Fri Feb 21 10:05:12 2020 HTTP 192.168.1.100:52780 -> 151.139.128.10:80 www.neopets.com GET /sbbi/?sbbpg=sbbShell&gprid=nO

    Example with predominantly TLS Traffic:

    Fri Feb 21 11:33:35 2020 TLS v1.2 192.168.1.100:50400 ->  31.13.71.36:443 www.facebook.com
    Fri Feb 21 11:33:35 2020 TLS v1.2 192.168.1.100:47124 ->  130.211.16.53:443 d.joinhoney.com
    Fri Feb 21 11:33:36 2020 TLS v1.2 192.168.1.100:48088 ->  130.211.26.229:443 s.joinhoney.com
    Fri Feb 21 11:33:36 2020 TLS v1.2 192.168.1.100:38796 ->  35.186.217.6:443 err.joinhoney.com
    Fri Feb 21 11:33:48 2020 HTTP 192.168.1.100:49528 -> 35.186.217.6:80 err.joinhoney.com GET /
    Fri Feb 21 11:33:48 2020 HTTP 192.168.1.100:49528 -> 35.186.217.6:80 err.joinhoney.com GET /favicon.ico
    Fri Feb 21 11:33:58 2020 TLS v1.2 192.168.1.100:36008 ->  104.244.42.1:443 twitter.com
    Fri Feb 21 11:33:59 2020 TLS v1.2 192.168.1.100:49254 ->  104.244.42.194:443 api.twitter.com


Please note: This will not work as intended with scapy or cryptography.
It will also not work without being run as root.
