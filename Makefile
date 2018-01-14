.PHONY: format mrproper

format: mrproper README.md

README.md: READ.ME TO.DO
	cat $< > $@
	echo -e "\n# TODO liste" >> $@
	echo TO.DO >> $@

mrproper:
	$(RM) -r *~ */*~ */*/*~
	$(RM) -r */__pycache__
