 alter table raw_data add college text;
 alter table raw_data add major text;
 alter table raw_data add FT text;
update raw_data set major='STEM'  , college='hofstra', FT='FT' where sheet_title='HofstraFT_STEM';
update raw_data set major='STEM'  , college='adelphi', FT='FT' where sheet_title='AdelphiFT_STEM';
update raw_data set major='BIO'  , college='hofstra', FT='FT' where sheet_title='HofstraFT_Bio';
update raw_data set major='BIO'  , college='adelphi', FT='FT' where sheet_title='AdelphiFT_Bio';

update raw_data set major='STEM'  , college='hofstra', FT='T' where sheet_title='HofstraTransfer_STEM';
update raw_data set major='STEM'  , college='adelphi', FT='T' where sheet_title='AdelphiTransfer_STEM';
update raw_data set major='BIO'  , college='hofstra', FT='T' where sheet_title='HofstraTransfer_Bio';
update raw_data set major='BIO'  , college='adelphi', FT='T' where sheet_title='AdelphiTransfer_Bio';

alter table file add column parts text[];
 update file set parts=regexp_split_to_array(filename,'_|\.|\-');