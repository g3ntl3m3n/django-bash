#!/bin/bash

if [ $1 = "create" ]; then
        mkdir ~/test
	if [ $? -eq 0 ]; then
    	echo "Dosya olusturma basarili.."
    	exit 0

	else
    	>&2 echo "Dosya olusturma basarisiz.."
    	exit 1
	fi

elif [ $1 = "delete" ]
then
   	rm -rf ~/test
        if [ $? -eq 0 ]; then
        echo "Dosya silme basarili.."
        exit 0

        else
        >&2 echo "Dosya silerken hata.."
        exit 1
        fi

else
  echo "Gecersiz Komut"
  exit 1

fi
