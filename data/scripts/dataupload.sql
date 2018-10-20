SET CLIENT_ENCODING TO 'utf8';
copy products(description,pricing,reviews,image) from 'C:\Users\tanmoy.chatterjee\eclipse-workspace\smart-retail\data\products.csv' DELIMITER ',' CSV HEADER;
copy amazonreviews from 'C:\Users\tanmoy.chatterjee\eclipse-workspace\smart-retail\data\amazonproductreviews.csv' DELIMITER ',' CSV HEADER;
