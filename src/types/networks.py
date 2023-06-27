from pydantic import PostgresDsn as Postgres


class PostgresDsn(Postgres):

    def __getitem__(self, item):
        if item in self.allowed_schemes:
            return self.build(
                scheme=item,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                path=self.path,
                query=self.query,
                fragment=self.fragment
            )
        raise ValueError('invalid scheme')
