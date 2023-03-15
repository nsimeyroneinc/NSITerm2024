#!/bin/bash
if [ $# -eq 0 ];then
    echo "usage : $0 NSI"
    exit 0
fi
DISCIPLINE="$1"
DISCIPLINE_JSON="${DISCIPLINE}.json"
MAX=200
wget "https://cyclades.education.gouv.fr/delos/api/public/sujets/ece?sort=libelle&order=ASC&page=0&itemsPerPage=${MAX}&globalFilter=${DISCIPLINE}" -O "${DISCIPLINE_JSON}"

cat "${DISCIPLINE_JSON}"|tr ",{" "\n\n"|grep '^"id"'|sort -u|cut -f 4 -d '"'|while read SUJET;do
    NAME=""
    FIRST="y"
    wget -q "https://cyclades.education.gouv.fr/delos/api/public/sujet/${SUJET}" -O -|tr "," "\n"|while read LIGNE;do
        if [ "${LIGNE:0:6}" == '"id":"' ];then
            if [ "$NAME" != "" ];then
                ID=$(echo "$LIGNE"|cut -f 4 -d '"')
                FULLNAME="${NAME}.py"
                if [ "$FIRST" == "y" ];then
                    FULLNAME="${NAME}.pdf"
                    FIRST=""
                fi
                echo "${ID} -> ${FULLNAME}"
                wget -q "https://cyclades.education.gouv.fr/delos/api/public/file/?idSujet=${SUJET}&fileName=${ID}" -O "${FULLNAME}"
           fi
        fi
        if [ "${LIGNE:0:7}" == '"cle":"' ];then
            NAME=$(echo "$LIGNE"|cut -f 4 -d '"')
        fi
    done
done