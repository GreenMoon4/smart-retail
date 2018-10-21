SET CLIENT_ENCODING TO 'utf8';
copy products(description,pricing,reviews,image) from '/Users/josuablejeru/repos/smart-retail/data/products.csv' DELIMITER ',' CSV HEADER;
copy amazonreviews from '/Users/josuablejeru/repos/smart-retail/data/amazonproductreviews.csv' DELIMITER ',' CSV HEADER;
