# coding: UTF-8

from core.status_invest import StatusInvest
import argparse


def main(args):
    status_invest = StatusInvest(args.tickers, args.international)
    status_invest.start()
    status_invest.finish()


if __name__ == "__main__":
    print(
        """
   SSSSSSSSSSSSSSS                           iiii          tttt         hhhhhhh
 SS:::::::::::::::S                         i::::i      ttt:::t         h:::::h
S:::::SSSSSS::::::S                          iiii       t:::::t         h:::::h
S:::::S     SSSSSSS                                     t:::::t         h:::::h
S:::::S               mmmmmmm    mmmmmmm   iiiiiiittttttt:::::ttttttt    h::::h hhhhh
S:::::S             mm:::::::m  m:::::::mm i:::::it:::::::::::::::::t    h::::hh:::::hhh
 S::::SSSS         m::::::::::mm::::::::::m i::::it:::::::::::::::::t    h::::::::::::::hh
  SS::::::SSSSS    m::::::::::::::::::::::m i::::itttttt:::::::tttttt    h:::::::hhh::::::h
    SSS::::::::SS  m:::::mmm::::::mmm:::::m i::::i      t:::::t          h::::::h   h::::::h
       SSSSSS::::S m::::m   m::::m   m::::m i::::i      t:::::t          h:::::h     h:::::h
            S:::::Sm::::m   m::::m   m::::m i::::i      t:::::t          h:::::h     h:::::h
            S:::::Sm::::m   m::::m   m::::m i::::i      t:::::t    tttttth:::::h     h:::::h
SSSSSSS     S:::::Sm::::m   m::::m   m::::mi::::::i     t::::::tttt:::::th:::::h     h:::::h
S::::::SSSSSS:::::Sm::::m   m::::m   m::::mi::::::i     tt::::::::::::::th:::::h     h:::::h
S:::::::::::::::SS m::::m   m::::m   m::::mi::::::i       tt:::::::::::tth:::::h     h:::::h
 SSSSSSSSSSSSSSS   mmmmmm   mmmmmm   mmmmmmiiiiiiii         ttttttttttt  hhhhhhh     hhhhhhh



IIIIIIIIII                                                                                 tttt
I::::::::I                                                                              ttt:::t
I::::::::I                                                                              t:::::t
II::::::II                                                                              t:::::t
  I::::Innnn  nnnnnnnn vvvvvvv           vvvvvvv eeeeeeeeeeee        ssssssssss   ttttttt:::::ttttttt
  I::::In:::nn::::::::nnv:::::v         v:::::vee::::::::::::ee    ss::::::::::s  t:::::::::::::::::t
  I::::In::::::::::::::nnv:::::v       v:::::ve::::::eeeee:::::eess:::::::::::::s t:::::::::::::::::t
  I::::Inn:::::::::::::::nv:::::v     v:::::ve::::::e     e:::::es::::::ssss:::::stttttt:::::::tttttt
  I::::I  n:::::nnnn:::::n v:::::v   v:::::v e:::::::eeeee::::::e s:::::s  ssssss       t:::::t
  I::::I  n::::n    n::::n  v:::::v v:::::v  e:::::::::::::::::e    s::::::s            t:::::t
  I::::I  n::::n    n::::n   v:::::v:::::v   e::::::eeeeeeeeeee        s::::::s         t:::::t
  I::::I  n::::n    n::::n    v:::::::::v    e:::::::e           ssssss   s:::::s       t:::::t    tttttt
II::::::IIn::::n    n::::n     v:::::::v     e::::::::e          s:::::ssss::::::s      t::::::tttt:::::t
I::::::::In::::n    n::::n      v:::::v       e::::::::eeeeeeee  s::::::::::::::s       tt::::::::::::::t
I::::::::In::::n    n::::n       v:::v         ee:::::::::::::e   s:::::::::::ss          tt:::::::::::tt
IIIIIIIIIInnnnnn    nnnnnn        vvv            eeeeeeeeeeeeee    sssssssssss              ttttttttttt
    """
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("tickers", nargs="+", type=str)
    parser.add_argument(
        "--international", action=argparse.BooleanOptionalAction, default=False
    )
    args = parser.parse_args()

    main(args)
