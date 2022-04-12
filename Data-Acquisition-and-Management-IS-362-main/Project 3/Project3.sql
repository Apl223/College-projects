SELECT FirstName,LastName, T.Name,A.Title from customer as C
JOIN invoice as IV on C.CustomerId = IV.CustomerId
JOIN invoiceline as IVL on IV.InvoiceId = IVL.InvoiceId
JOIN track as T on IVL.TrackId = T.TrackId
JOIN album as A on T.AlbumId = A.AlbumId
order by FirstName,LastName;

