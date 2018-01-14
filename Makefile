.PHONY: format mrproper

format: mrproper README.md

README.md: READ.ME TO.md
	cat $< > $@
	echo -e "\n# TODO liste" >> $@
	cat TO.md >> $@

mrproper:
	$(RM) -r *~ */*~ */*/*~
	$(RM) -r */__pycache__
