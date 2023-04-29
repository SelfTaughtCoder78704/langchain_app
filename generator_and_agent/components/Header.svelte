

<script>
  export let title = '';
  export let subtitle = '';
  export let image = '';
  export let class = 'header';
</script>

<div class={class}>
  <h1>{title}</h1>
  <h2>{subtitle}</h2>
  <img src={image} />
</div>