for f in *.pdf; do
    if ! pdfinfo "$f" &> /dev/null; then
        echo "$f" is broken
    fi
done
