def diff_of_n_root_error(y, y_hat, n, p):
     y_root = pow(y, (1/n))
     y_hat_root = pow(y_hat, (1/n))
     diff_of_nRE = y_root - y_hat_root
     loss = pow(diff_of_nRE, p)
     print(diff_of_nRE)

diff_of_n_root_error(y=100 , y_hat=99.5 , n=2 , p=1)
diff_of_n_root_error(y=50 , y_hat=49.5 , n=2 , p=1)
diff_of_n_root_error(y=20 , y_hat=19.5 , n=2 , p=1)
diff_of_n_root_error(y=0.6 , y_hat=0.1 , n=2 , p=1)